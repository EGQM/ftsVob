#coding: utf-8
import logging

class DefaultLogHandler(object):
    """默认的Log类基础系统支持类"""
    def __init__(self, name='mylog', filepath='default.log', log_type='stdout', log_level='DEBUG'):
        self.logger = logging.getLogger(name)
        self.loglevel = {'CRITICAL': logging.CRITICAL,
                         'ERROR': logging.ERROR,
                         'WARNING': logging.WARNING,
                         'INFO': logging.INFO,
                         'DEBUG': logging.DEBUG}

        self.logger.setLevel(self.loglevel[log_level])
        fmt = logging.Formatter(fmt='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')

        if log_type == 'stdout':
            # 创建一个handler，用于标准输出
            ch = logging.StreamHandler()
            ch.setFormatter(fmt)
            self.logger.addHandler(ch)
        if log_type == 'file':
            # 创建一个handler，用于输出日志文件
            fh = logging.FileHandler(filepath)
            fh.setFormatter(fmt)
            self.logger.addHandler(fh)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)

    def warn(self, *args, **kwargs):
        self.logger.warning(*args, **kwargs)

    def critical(self, *args, **kwargs):
        self.logger.critical(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)
        
