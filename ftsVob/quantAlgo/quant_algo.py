#coding: utf-8
import datetime
import time
from threading import Thread
from ..quantEngine.quant_constant import *
from ..quantGateway.quant_gateway import *

"""
GateWay的上层封装
这里实现了一些算法交易的类
Engine层和Strategy层只和算法交易层交互
"""

class AlgoTrade(object):
    """算法交易接口"""
    def __init__(self, gateWay, eventEngine, log=None):
        """Constructor"""
        self.gateway = gateWay
        self.eventengine = eventEngine
        self.log = log
        self.orderinfo = {}

    def twap(self, size, volume, reqobj, price=0, interval=1, maxtimeout=60):
        self.twap_thread = Thread(target=self.twap_callback, args=(size, volume, reqobj, price, interval, maxtimeout))
        self.twap_thread.start()

    def vwap(self, size, volume, reqobj, price=0, interval=1, maxtimeout=60):
        self.vwap_thread = Thread(target=self.vwap_callback, args=(size, volume, reqobj, price, interval, maxtimeout))
        self.vwap_thread.start()

    def twap_callback(self, size, volume, reqobj, price, interval, maxtimeout):
        """Time Weighted Average Price
        每次以线程模式调用
        @size: 小单规模
        @volume: 总单规模
        @reqobj: 发单请求
        @price: 下单价格，默认为0表示按照bid1下单
        @interval: 时间结果，每个size的时间间隔
        @maxtimeout: 最长等待时间，超时则按照ask1扫单
        """
        starttime = datetime.datetime.now()
        status_send_order = {'timeout':False, 'success':False}
        while(True):
            if volume % size > 0:
                count = volume // size + 1
            else:
                count = volume // size

            #获取合约的即时价格，目前单一API只能处理单个合约
            rb_data = self.gateway.tickdata[reqobj.symbol].tolist()[-1]
            price = rb_data.bidPrice1
            
            for i in range(count):
                if i == count-1:
                    reqobj.volume = (volume - (i+1)*size) 
                    reqobj.price = price
                    self.gateway.sendOrder(reqobj)
                else:
                    reqobj.volume = size
                    reqobj.price = price
                    self.gateway.sendOrder(reqobj)
                time.sleep(interval)

             #检查Order信息表，准备撤单
             remain_volume = 0
             for elt in self.orderinfo:
                 of = orderinfo[elt]
                 if of.status != STATUS_ALLTRADED:
                     cancel_obj = VtCancelOrderReq()
                     cancel_obj.symbol = of.symbol
                     cancel_obj.exchange = of.exchange
                     cancel_obj.orderID = of.orderID
                     cancel_obj.frontID = of.frontID
                     cancel_obj.sessionID = of.sessionID
                     self.gateway.cancelOrder(cancel_obj)
                     remain_volume = of.totalVolume - of.tradedVolume

             if remain_volume == 0:
                 status_send_order['success'] = True
                 status_send_order['timeout'] = False
                 break
                 
             #记录剩余合约量，准备下一轮下单
             volume = remain_volume
             endtime = datetime.datetime.now()
             if (endtime - starttime).seconds > maxtimeout:
                 status_send_order['timeout'] = True
                 status_send_order['success'] = False
                 break
             
        #剩余单数以对手价格下单
        rb_data = self.gateway.tickdata[reqobj.symbol].tolist()[-1]
        price = rb_data.AskPrice1
        reqobj.price = price
        reqobj.volume = volume
        self.gateway.sendOrder(reqobj)
        
    def get_order_info_callback(self, event):
        orderinfo = event.data
        self.orderinfo[orderinfo.orderID] = orderinfo

    def get_trade_info_callback(self, event):
        tradeinfo = event.data
        self.orderinfo[tradeinfo.orderID].status = STATUS_ALLTRADED

    def register(self):
        self.eventEngine.register(EVENT_TRADE, self.get_trade_info_callback)
        self.eventEngine.register(EVENT_ORDER, self.get_order_info_callback)
        
    def vwap_callback(self, size, volume, reqobj, price, interval, maxtimeout):
        pass
        
        
        
        
