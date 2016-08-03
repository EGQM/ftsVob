# encoding: UTF-8

import sys
import os
import ctypes
import platform

from vtEngine import MainEngine

#----------------------------------------------------------------------
def main():
    """主程序入口"""
    # 重载sys模块，设置默认字符串编码方式为utf8
    reload(sys)
    with open('vntrade.pid', 'w') as f:
        f.write(str(os.getpid()))
    sys.setdefaultencoding('utf8')
    
    # 初始化主引擎和主窗口对象
    mainEngine = MainEngine()
    mainEngine.connect('CTP')

if __name__ == '__main__':
    main()
