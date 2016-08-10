#coding: utf-8
import os
import sys
import time
import importlib

from collections import OrderedDict
from .event_engine import EventEngine
from .push_engine import DefaultQuotationEngine
from .push_engine import AccountInfoEngine

#引用系统支持类
from ..logHandler import DefaultLogHandler
from ..quantGateway import *

class MainEngine:
    """主引擎，负责行情 / 事件驱动引擎 / 交易"""

    def __init__(self, gateway_name, gateway_config, log_handler=DefaultLogHandler(), quotation_engines=None):
        """初始化事件引擎 / 连接gateway"""
        self.event_engine = EventEngine()
        self.gateway = Use(gateway_name, gatewayConf=gateway_config, eventEngine=self.event_engine, log=log_handler)
        self.log = log_handler
        if os.path.exists(gateway_config):
            self.gateway.connect()
        else:
            self.log.warn(u"配置文件不存在 %s" % gateway_config)

        quotation_engines = quotation_engines or [AccountInfoEngine]

        if type(quotation_engines) != list:
            quotation_engines = [quotation_engines]
        self.quotation_engines = []
        for quotation_engine in quotation_engines:
            self.quotation_engines.append(quotation_engine(self.event_engine, self.gateway))

        #保存读取的策略类
        self.strategies = OrderedDict() 
        self.strategy_list = list()

        self.log.info(u'启动主引擎')

    def start(self):
        """启动主引擎"""
        self.event_engine.start()
        #策略引擎延时启动,保证交易所服务器连接成功
        time.sleep(5)
        for quotation_engine in self.quotation_engines:
            quotation_engine.start()

    def load_strategy(self, names=None):
        """动态加载策略
        暂时不提供reload策略的功能
        @param names: 策略名列表"""
        
        s_folder = 'strategies'
        strategies = os.listdir(s_folder)
        strategies = filter(lambda file: file.endswith('.py') and file != '__init__.py', strategies)
        importlib.import_module(s_folder)
        for strategy_file in strategies:
            strategy_module_name = os.path.basename(strategy_file)[:-3]
            strategy_module = importlib.import_module('.' + strategy_module_name, 'strategies')
            strategy_class = getattr(strategy_module, 'Strategy')
            if names is None or strategy_class.name in names:
                self.strategies[strategy_module_name] = strategy_class
                self.strategy_list.append(strategy_class(self.gateway, log_handler=self.log, main_engine=self))
                self.log.info(u'加载策略: %s' % strategy_module_name)

        for strategy in self.strategy_list:
            for quotation_engine in self.quotation_engines:
                self.event_engine.register(quotation_engine.EventType, strategy.run)
        self.log.info(u'加载策略完毕')

