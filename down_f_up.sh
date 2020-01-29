#list the files 
aws s3 ls s3://c-res-stg/s1/tables/f1592746-ba94-404c-8021-789630e0c8bd/d_month=2019-12/ --profile reseller>mf.txt

#take oout only file name 
cut mf.txt -c 32- > mf1.txt

#copy here 

while IPS= read -r file; do aws s3 cp s3://c-res-stg/s1/tables/f1592746-ba94-4
04c-8021-789630e0c8bd/d_month=2020-01/"$file" . ; done < mf1.txt 

#$upload to new account 
while IPS= read -r file; 
do aws s3 cp "$file" s3://c-res-stg-d/tables/c_res_fin_d_p1/d_month=2019-12/ 
--profile ge_1; done < mf1.txt 



