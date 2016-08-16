#coding: utf-8
from ftsVob.quantGateway.quant_constant import *
from ftsVob.quantGateway.quant_gateway import  *

from ftsVob import  StrategyTemplate
from ftsVob import  DefaultLogHandler
from ftsVob import  AlgoTrade

class Strategy(StrategyTemplate):
    name = 'Cta strategy'

    def strategy(self, event):
        self.log.info(u'Cta 策略触发')
        self.log.info(event.data)
        self.log.info('\n')

    def log_handler(self):
        return DefaultLogHandler(name=__name__, log_type='file')
    
    def run(self, event):
        self.log.info(event.data)
        orderreq = VtOrderReq()
        orderreq.symbol = 'IF1609'
        orderreq.volume = 5 
        orderreq.priceType = PRICETYPE_FOK
        orderreq.direction = DIRECTION_SHORT
        orderreq.offset = OFFSET_OPEN
        self.algo.twap(1, orderreq)
        """
        if 'position' in event.data:
            poslist = event.data['position']
            for elt in poslist:
                if elt['PosiDirection'] == '3':
                    direct = DIRECTION_LONG
                if elt['PosiDirection'] == '2':
                    direct = DIRECTION_SHORT
                offset = OFFSET_CLOSE
                if elt['Position'] > 0:
                    req = ReqObj(elt['InstrumentID'], 
                                 elt['SettlementPrice'],
                                 elt['Position'],
                                 PRICETYPE_FOK,
                                 direct,
                                 offset)
                    self.gateway.sendOrder(req)
                else:
                    self.log.info('Position volume is zero')
        """

