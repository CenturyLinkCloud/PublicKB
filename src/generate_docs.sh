#/bin/bash

pydoc -w clc clc.{account,api,billing,blueprint,cli,group,network,output,queue,server,shell,user}
perl -p -i -e "s/keithresar//" *html

echo git checkout gh-pages
echo mv *html ../src/
