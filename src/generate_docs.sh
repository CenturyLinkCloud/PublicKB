#/bin/bash

pydoc -w clc \
		 clc.APIv1 clc.APIv2 \
         clc.APIv1.{account,api,billing,blueprint,cli,group,network,output,queue,server,shell,user} \
         clc.APIv2.{public_ip,disk,account,alert,anti_affinity,api,datacenter,group,network,queue,server,template,time_utils}
perl -p -i -e "s/keithresar//g" *html

echo "Manual step  > git checkout gh-pages"
echo "Manual step  > mv *html ../doc/"
