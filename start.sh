#!/bin/bash
service redis-server restart
cd /www
ipadd=`ifconfig eth0 | egrep "inet \S+"|awk '{print $2}'`
if [ -f manage.py ]
then
	python3 manage.py runserver $ipadd:8000
fi

