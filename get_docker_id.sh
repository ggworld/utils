docker ps | grep "worker" | awk '{print $1}'

# and with Sasha insight:
docker exec -it $(docker ps | grep "worker" | awk '{print $1}' | xargs -I% echo "%") bash

# and with user airflow
docker exec -it -u airflow $(docker ps | grep "worker" | awk '{print $1}' | xargs -I% echo "%") bash
