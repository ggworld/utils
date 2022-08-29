#in the background 
#               database url                 tunnel ip  public key -g yes yo except connections on all Ips  
ssh -N -L 3306:10.10.10.99:3306  menachem@x.x.x.x -i k_g_1f1 -f -g yes


#open prompt:
ssh -N -L 3306:x.x.x.x:3306  menachem@x.x.x.x -i k_g_1f1 -f


#and for port :
ssh -i data-engineer-gad-01.pem ec2-user@193.45.14.9 -N -L 9999:10.0.109.211:8000    
