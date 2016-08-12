Daomon program of ftsVob (Future Trade System Vob)
Author: Occ
Guide:
* Server trade type system type, has no graphic user interface
* Platform is build on ubuntu14.0+ and python2.7+
* python ftsMain.py is will starting whole trade system, and will configure ctp.json under current directory
* Need combile vnctpmd.so,vnctptd.so on your own platform and install in ftsVob/quantGateway/ctpGateway directory

### Program whole picture

.
 * [strategies](./strategies)
   * [demo.py](./strategies/demo.py)
   * [__init__.py](./strategies/__init__.py)
 * [daemonvt.sh](./daemonvt.sh)
 * [ctp.json](./ctp.json)
 * [ftsVob](./ftsVob)
   * [quantEngine](./ftsVob/quantEngine)
     * [event_engine.py](./ftsVob/quantEngine/event_engine.py)
     * [push_engine](./ftsVob/quantEngine/push_engine)
       * [account_info_engine.py](./ftsVob/quantEngine/push_engine/account_info_engine.py)
       * [base_engine.py](./ftsVob/quantEngine/push_engine/base_engine.py)
       * [clock_engine.py](./ftsVob/quantEngine/push_engine/clock_engine.py)
       * [__init__.py](./ftsVob/quantEngine/push_engine/__init__.py)
       * [quotation_engine.py](./ftsVob/quantEngine/push_engine/quotation_engine.py)
     * [main_engine.py](./ftsVob/quantEngine/main_engine.py)
     * [__init__.py](./ftsVob/quantEngine/__init__.py)
   * [quantGateway](./ftsVob/quantGateway)
     * [ctpGateway](./ftsVob/quantGateway/ctpGateway)
       * [ctpGateway.py](./ftsVob/quantGateway/ctpGateway/ctpGateway.py)
       * [vnctpmd.so](./ftsVob/quantGateway/ctpGateway/vnctpmd.so)
       * [vnctptd.so](./ftsVob/quantGateway/ctpGateway/vnctptd.so)
       * [ctpDataType.py](./ftsVob/quantGateway/ctpGateway/ctpDataType.py)
       * [__init__.py](./ftsVob/quantGateway/ctpGateway/__init__.py)
     * [quant_gateway.py](./ftsVob/quantGateway/quant_gateway.py)
     * [api.py](./ftsVob/quantGateway/api.py)
     * [__init__.py](./ftsVob/quantGateway/__init__.py)
     * [quant_constant.py](./ftsVob/quantGateway/quant_constant.py)
   * [logHandler](./ftsVob/logHandler)
     * [default_handler.py](./ftsVob/logHandler/default_handler.py)
     * [__init__.py](./ftsVob/logHandler/__init__.py)
   * [quantStrategy](./ftsVob/quantStrategy)
     * [__init__.py](./ftsVob/quantStrategy/__init__.py)
     * [strategyTemplate.py](./ftsVob/quantStrategy/strategyTemplate.py)
   * [databaseSys](./ftsVob/databaseSys)
   * [__init__.py](./ftsVob/__init__.py)
 * [ftsMain.py](./ftsMain.py)

### Develop plan
* Improve log handler system need fix some bugs of log system
* Adding database api, such as mysql, mongodb, redis
* Adding trading interface which is needed by concrete strategy

