#coding: utf-8
from collections import defaultdict
from Queue import Queue, Empty
from threading import Thread

#帐户相关常量事件
EVENT_POSITION = 'ePosition'
EVENT_ACCOUNT = 'eAccount'

class Event:
    """事件对象"""

    def __init__(self, event_type, data=None, queue_type='td'):
        self.event_type = event_type
        self.data = data
        self.queue_type = queue_type

class EventEngine:
    """事件驱动引擎"""

    def __init__(self):
        """初始化事件引擎"""
        # 事件队列,行情队列和交易队列分开
        self.__queue_td = Queue()
        self.__queue_md = Queue()

        # 事件引擎开关
        self.__active = False

        # 事件引擎处理线程
        self.__thread = Thread(target=self.__run)

        # 事件字典，key 为时间， value 为对应监听事件函数的列表
        self.__handlers = defaultdict(list)

    def __run(self):
        """启动引擎"""
        while self.__active:
            try:
                event_td = self.__queue_td.get(block=True, timeout=1)
                event_md = self.__queue_md.get(block=True, timeout=1)
                
                handle_thread_td = Thread(target=self.__process, args=(event_td,))
                handle_thread_md = Thread(target=self.__process, args=(event_md,))
                
                handle_thread_td.start()
                handle_thread_md.start()
            except Empty:
                pass

    def __process(self, event):
        """事件处理"""
        # 检查该事件是否有对应的处理函数
        if event.event_type in self.__handlers:
            # 若存在,则按顺序将时间传递给处理函数执行
            for handler in self.__handlers[event.event_type]:
                handler(event)

    def start(self):
        """引擎启动"""
        self.__active = True
        self.__thread.start()

    def stop(self):
        """停止引擎"""
        self.__active = False
        self.__thread.join()

    def register(self, event_type, handler):
        """注册事件处理函数监听"""
        if handler not in self.__handlers[event_type]:
            self.__handlers[event_type].append(handler)

    def unregister(self, event_type, handler):
        """注销事件处理函数"""
        handler_list = self.__handlers.get(event_type)
        if handler_list is None:
            return
        if handler in handler_list:
            handler_list.remove(handler)
        if len(handler_list) == 0:
            self.__handlers.pop(event_type)

    def put(self, event):
        if event.queue_type == 'td':
            self.__queue_td.put(event)
        if event.queue_type == 'md':
            self.__queue_md.put(event)

    @property
    def queue_td_size(self):
        return self.__queue_td.qsize()

    @property
    def queue_md_size(self):
        return self.__queue_md.qsize()
