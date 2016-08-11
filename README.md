Daomon program of ftsVob (Future Trade System Vob)
Author: Occ
Guide:
* Server trade type system type, has no graphic user interface
* Platform is build on ubuntu14.0+ and python2.7+
* python ftsMain.py is will starting whole trade system, and will configure ctp.json under current directory
* Need combile vnctpmd.so,vnctptd.so on your own platform and install in ftsVob/quantGateway/ctpGateway directory

### Program whole picture

ctp.json
ftsMain.py
strategies/
    --->demo.py(example strategy only read account info and position)
ftsVob
    --->quantEngine/
        --->main_engine.py
        --->event_engine.py
        --->push_engine/
            --->base_engine.py
            --->clock_engine.py
            --->XXX_engine.py
    --->quantGateway/
            --->quant_gateway.py
            --->quant_constant.py
            --->ctpGateway/ (Trade interface mode)
    --->quantStrategy/
            --->strategyTemplate.py
    --->logHandler/
            --->default_handler.py
    --->databaseSys/

### Develop plan
* Improve log handler system need fix some bugs of log system
* Adding database api, such as mysql, mongodb, redis
* Adding trading interface which is needed by concrete strategy

