#coding: utf-8
from .ctpGateway import CtpGateway 

def Use(gatewayname, **kwargs):
    """用于生成特定的交易接口模块
    :param gatewayname: 期货交易接口支持['ctp', 'lts']
    :return 对应的交易接口类
    """
    if gatewayname.lower() in ['ctp', 'CTP']:
        return CtpGateway(**kwargs)
