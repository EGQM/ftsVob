#coding: utf-8
from ftsVob import  StrategyTemplate
from ftsVob import  DefaultLogHandler

class Strategy(StrategyTemplate):
    name = 'Ctp strategy'

    def strategy(self, event):
        self.log.info(u'Cta 策略触发')
        self.log.info(event.data)
        self.log.info('\n')

    def log_handler(self):
        return DefaultLogHandler(name='ctp', log_type='file')
