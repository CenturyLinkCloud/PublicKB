#!/bin/bash

CLC=../clc/src/clc.py
CONFIG=../clc/src/config.ini
ALIAS=KRAP




SERVERNAME=`$CLC -qq -c $CONFIG --format text servers create --alias $ALIAS --template CENTOS-6-64-TEMPLATE --name KNIFE \
	 --description "Chef Knife Deploy Test" --cpu 1 --ram 1 --location UC1 --group Test1 --network vlan_266_10.120.66`
echo "`date`: DEPLOYED $SERVERNAME"

PASSWORD=`$CLC -qq -c $CONFIG --cols=Password --format text servers get-credentials --alias $ALIAS --server $SERVERNAME`

IP=`$CLC -qq -c $CONFIG --cols=IPAddress --format text servers get --alias $ALIAS --server $SERVERNAME`
echo "`date` IP $IP"

knife bootstrap $IP -x root -P $PASSWORD --sudo

