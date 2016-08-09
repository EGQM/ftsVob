# coding: utf-8
from threading import Thread

import time
from ..event_engine import Event


class BaseEngine:
    """行情推送引擎基类"""
    EventType = 'base'
    PushInterval = 1

    def __init__(self, event_engine, gateway):
        self.event_engine = event_engine
        self.is_active = True
        self.quotation_thread = Thread(target=self.push_quotation)
        self.quotation_thread.setDaemon(False)
        self.gateway = gateway
        self.init()

    def start(self):
        self.quotation_thread.start()

    def stop(self):
        self.is_active = False

    def push_quotation(self):
        while self.is_active:
            try:
                response_data = self.fetch_quotation()
            except:
                time.sleep(self.PushInterval)
                continue
            event = Event(event_type=self.EventType, data=response_data)
            self.event_engine.put(event)
            time.sleep(self.PushInterval)

    def fetch_quotation(self):
        # return your quotation
        return None

    def init(self):
        # do something init
        pass
