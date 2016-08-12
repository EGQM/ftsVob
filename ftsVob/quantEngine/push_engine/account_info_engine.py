#coding: utf-8

import json
import time
from .base_engine import BaseEngine
from ..event_engine import *

class AccountInfoEngine(BaseEngine):
    """处理帐户信息引擎将帐户所有信息打包发给策略"""
    EventType = 'account'
    PushInterval = 10
    
    def init(self):
        #暂时作为测试数据
        self.source = {}
        self.register()
        
    def register(self):
        #注册需要的数据推送事件
        self.event_engine.register(EVENT_POSITION, self.get_position)
        self.event_engine.register(EVENT_ACCOUNT, self.get_account)

    def get_position(self, event):
        self.source['position'] = event.data

    def get_account(self, event):
        self.source['account'] = json.dumps(event.data.__dict__)
        
    def fetch_quotation(self):
        #self.gateway.qryAccount()
        #这里需要延时处理,否则回报会丢弃,建议使用多引擎的方式
        self.gateway.qryPosition()
        return self.source
