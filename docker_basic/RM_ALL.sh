docker ps -a
docker rm -vf $(docker ps -aq)
docker ps -a

docker images
docker rmi -f $(docker images -aq)
docker images
