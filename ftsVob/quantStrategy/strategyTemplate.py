# coding:utf-8
import sys
import traceback

from ..quantAlgo import AlgoTrade

class StrategyTemplate:
    name = 'DefaultStrategyTemplate'

    def __init__(self, gateway, log_handler, main_engine):
        self.gateway = gateway
        self.main_engine = main_engine

        # 优先使用自定义 log 句柄, 否则使用主引擎日志句柄
        self.log = self.log_handler() or log_handler

        # 每个策略对应一个Algo类
        self.algo = AlgoTrade(gateway, main_engine.event_engine)

        self.init()

    def init(self):
        # 进行相关的初始化操作
        pass

    def strategy(self, event):
        pass

    def run(self, event):
        try:
            self.strategy(event)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.log.error(repr(traceback.format_exception(exc_type,
                                                           exc_value,
                                                           exc_traceback)))

    def clock(self, event):
        pass

    def log_handler(self):
        """
        优先使用在此自定义 log 句柄, 否则返回None, 并使用主引擎日志句柄
        :return: log_handler or None
        """
        return None
