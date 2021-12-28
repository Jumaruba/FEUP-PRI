sudo docker rm -f $(sudo docker ps -a -q)
sudo docker-compose up -d --build