docker ps -a
docker rm -vf $(docker ps -aq)
docker ps -a
