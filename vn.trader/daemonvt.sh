#!/bin/bash
SCRIPTNAME=daemonvt.sh
PIDFILE=vntrade.pid
PYTHONCMD=/usr/bin/python
do_start() {
    $PYTHONCMD vtMain.py
}
do_stop() {
    kill `cat $PIDFILE` || echo -n "vntrade not running"
}
case "$1" in
    start)
        do_start
    ;;
    stop)
        do_stop
    ;;
    restart)
        do_stop
        do_start
    ;;
    *)
    echo "Usage: $SCRIPTNAME {start|stop||restart}" >&2
    exit 3
    ;;
esac
exit
