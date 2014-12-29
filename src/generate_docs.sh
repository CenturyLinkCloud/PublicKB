#/bin/bash

pydoc -w clc clc.APIv1.{account,api,billing,blueprint,cli,group,network,output,queue,server,shell,user}
perl -p -i -e "s/keithresar//g" *html

echo "Manual step  > git checkout gh-pages"
echo "Manual step  > mv *html ../src/"
