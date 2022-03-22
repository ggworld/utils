docker ps | grep "worker" | awk '{print $1}'

# and with Sasha insight:
docker exec -it $(docker ps | grep "worker" | awk '{print $1}' | xargs -I% echo "%") bash
