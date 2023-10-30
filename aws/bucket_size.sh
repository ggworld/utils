for namei in $(aws s3 ls | awk '{print $3}'); do echo -n $namei; echo -n " " ; aws s3 ls s3://$namei --recursive --human-readable --summarize | grep "Total Si" ; done > my_b_l.txt
