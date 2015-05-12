#! /bin/sh
# Creates single CSV of all servers from all locations within a Parent account and each of its Active subaccounts.

# https://github.com/CenturyLinkCloud/clc-python-sdk/blob/master/src/example_config.ini
config=example_config.ini

timestamp=`date +%Y%m%d-%H%M%S`
path=`dirname $0`
cd "$path"
script_dir=`pwd`

active_accounts=`clc --config $config --format csv accounts list | awk -F',' '$5=="True" {print $1}'`

Count=-1
aliasarray=(`echo $active_accounts`)
InstanceCount2=`echo ${#aliasarray[@]}`
InstanceCount=$(($InstanceCount2-1))

parent_account=`echo ${aliasarray[0]}`

echo "AccountAlias,Name,Description,HardwareGroupUUID,Cpu,MemoryGB,Status,ServerType,OperatingSystem,Location,IPAddress" > total_server_list.$parent_account.$timestamp.csv

until [ "$Count" -ge "$InstanceCount" ]; do
  let Count+=1

  current_alias=`echo ${aliasarray[$Count]}`
  clc --cols Name Description HardwareGroupUUID Cpu MemoryGB Status ServerType OperatingSystem Location IPAddress --config $config --format csv servers list-all --alias $current_alias > $parent_account-$current_alias-servers.csv
  sed -e '1,/^Name,Description/d' $parent_account-$current_alias-servers.csv | sed -e 's/^/'$current_alias',/' >> total_server_list.$parent_account.$timestamp.csv

echo
done

cat total_server_list.$parent_account.$timestamp.csv
