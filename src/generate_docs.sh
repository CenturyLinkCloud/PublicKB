#/bin/bash

pydoc -w clc clc.{account,api,billing,blueprint,cli,group,network,output,queue,server,shell,user}
mv *html ../doc/
