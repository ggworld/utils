 for namei in $(aws s3 ls | awk '{print $3}'); do aws s3 ls s3://$namei --recursive --human-readable --summarize | grep "Total Size:"; done > my_b_l.txt
