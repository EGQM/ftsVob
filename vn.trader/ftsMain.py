#coding: utf-8

import os
import ftsVob

def main():
    """期货交易系统的主程序入口"""
    """系统平台为Ubuntu 16.0+,python2.7+"""
    """后期可能需要迁移到python3.0+"""

    #暂时使用写定的gateway接口之后可能需要配置文件
    gatewayname = 'CTP'
    gatewayconfig = 'ctp.json'

    #输出程序pid
    with open('fts.pid', 'w') as f:
        f.write(str(os.getpid()))
    m = ftsVob.MainEngine(gatewayname, gatewayconfig)

    #加载策略
    m.load_strategy()
    
    #启动主引擎
    m.start()

if __name__ == '__main__':
    main()
