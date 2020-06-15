 kill -9 $(ps -ef | grep Tunnel | cut -c 7-13)
 
 kill -9 $(ps -ef | grep Tunnel |  awk '{print $2}')
 
