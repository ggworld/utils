 for i in  $(aws s3 ls 's3://<>-us-east-1-tier1/sap/2021-08-27'| awk -F ' +' '{print $4}'); 
 do aws s3 cp s3://<>-us-east-1-tier1/sap/$i s3://<>-us-east-1-data/wip/test/$i ;
 done
 
 
 
 
 
