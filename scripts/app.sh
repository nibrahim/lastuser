#!/bin/sh

# Management script for Lastuser instance Managed by system monit. 

# If you change any of these file locations, please make corresponding
# changes in the /etc/monit/conf.d/frp.conf file on the server. The
# local file scripts/monit/frp.conf is what you should change and
# deploy if you want to do this.

VENV=/opt/frp/environments/lastuser
APP_ROOT=/opt/lastuser/deployed
PID_FILE=/opt/lastuser/lastuser.pid
ACCESS_LOG_FILE=/var/log/frp/lastuser-gunicorn.access.log
ERROR_LOG_FILE=/var/log/frp/lastuser-gunicorn.error.log

FRP_CONFIG=production

# Activate virtualenv
. ${VENV}/bin/activate

case $1 in
   start)
      gunicorn --chdir ${APP_ROOT}/frp \
	  -D \
	  -p ${PID_FILE} \
	  --access-logfile=${ACCESS_LOG_FILE} \
	  --error-logfile=${ERROR_LOG_FILE} \
	  --log-level=debug \
	  wsgi:application
      ;;
    stop)  
      kill `cat ${PID_FILE}` ;;
    *)  
      echo "usage: app.sh {start|stop}" ;;
esac
exit 0
