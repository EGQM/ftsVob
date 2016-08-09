# coding: utf-8

from .base_engine import BaseEngine

class DefaultQuotationEngine(BaseEngine):
    """行情推送引擎"""
    EventType = 'quotation'

    def init(self):
        self.quotadata = self.gateway.subscribe('IF1608')

        #暂时作为测试数据
        self.source = {}

    def fetch_quotation(self):
        return self.source
