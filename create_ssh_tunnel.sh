#in the background 
#               database url                 tunnel ip        public key 
ssh -N -L 3306:10.10.10.99:3306  menachem@x.x.x.x -i k_g_1f1 -f


#open prompt:
ssh -N -L 3306:x.x.x.x:3306  menachem@x.x.x.x -i k_g_1f1 -f
