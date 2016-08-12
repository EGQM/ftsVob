Daomon program of ftsVob (Future Trade System Vob)
Author: Occ
Guide:
* Server trade type system type, has no graphic user interface
* Platform is build on ubuntu14.0+ and python2.7+
* python ftsMain.py is will starting whole trade system, and will configure ctp.json under current directory
* Need combile vnctpmd.so,vnctptd.so on your own platform and install in ftsVob/quantGateway/ctpGateway directory

### Program whole picture

 * [strategies]
   * [demo.py]
   * [__init__.py]
 * [daemonvt.sh]
 * [ctp.json]
 * [ftsVob]
   * [quantEngine]
     * [event_engine.py]
     * [push_engine]
       * [account_info_engine.py]
       * [base_engine.py]
       * [clock_engine.py]
       * [__init__.py]
       * [quotation_engine.py]
     * [main_engine.py]
     * [__init__.py]
   * [quantGateway]
     * [ctpGateway]
       * [ctpGateway.py]
       * [vnctpmd.so]
       * [vnctptd.so]
       * [ctpDataType.py]
       * [__init__.py]
     * [quant_gateway.py]
     * [api.py]
     * [__init__.py]
     * [quant_constant.py]
   * [logHandler]
     * [default_handler.py]
     * [__init__.py]
   * [quantStrategy]
     * [__init__.py]
     * [strategyTemplate.py]
   * [databaseSys]
   * [__init__.py]
 * [ftsMain.py]

### Develop plan
* Improve log handler system need fix some bugs of log system
* Adding database api, such as mysql, mongodb, redis
* Adding trading interface which is needed by concrete strategy

