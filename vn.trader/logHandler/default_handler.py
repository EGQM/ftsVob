#coding: utf-8
import os
import logging

logging.basicConfig(level=logging.DEBUG)

class DefaultLogHandler(object):
    """默认的Log类基础系统支持类"""
    
    def __init__(self, name='default', log_type='stdout', filepath='default.log', loglevel='DEBUG'):
        """Log对象
        :param name: log 实例名字
        :param :logtype: 'stdout' 输出到屏幕, 'file' 输出到指定文件
        :param :filename: log 文件名
        :param :loglevel: 设定log等级 ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']
        :return log handler object
        """

        self.log = logging.getLogger(name)
        self.loglevel = {'CRITICAL': logging.CRITICAL,
                         'ERROR': logging.ERROR,
                         'WARNING': logging.WARNING,
                         'INFO': logging.INFO,
                         'DEBUG': logging.DEBUG}

         
        fmt = logging.Formatter(fmt='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')


        if log_type == 'stdout':
            #创建一个handler输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(self.loglevel[loglevel])
            ch.setFormatter(fmt)
            self.log.addHandler(ch)
        if log_type == 'file':
            #创建一个handler输出到文件
            fh = logging.FileHandler(filepath)
            fh.setLevel(self.loglevel[loglevel])
            fh.setFormatter(fmt)
            self.log.addHandler(fh)

    def error(self, *args, **kwargs):
        self.log.error(*args, **kwargs)

    def debug(self, *args, **kwargs):
        self.log.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        self.log.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self.log.warning(*args, **kwargs)

    def critical(self, *args, **kwargs):
        self.log.critical(*args, **kwargs)

def main():
    dl = DefaultLogHandler()
    dl.info(u'测试')

if __name__ == '__main__':
    main()

