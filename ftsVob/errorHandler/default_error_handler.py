#coding: utf-8

"""
ftsVob的错误处理类
根据错误代码提供封装的回调函数
"""

class ErrorHandler(object):
    """错误处理句柄"""
    def __init__(self, log=None):
        self.log = log
        self.value_call = {
           31: self.err_lack_capital,
           15: self.err_field,
           90: self.err_search_wait
        }

    def process_error(self, event):
        """注册函数"""
        err = event.data
        self.value_call.get(err.errorID)(event)

    def err_lack_capital(self, event):
        self.log.info(event.data.errorMsg)

    def err_field(self, event):
        self.log.info(event.data.errorMsg)

    def err_search_wait(self, event):
        self.log.info(event.data.errorMsg)
         
        
