FROM stretch:latest
RUN apt-get update
RUN apt-get install -y python3
sudo apt-get install mosquitto -v
RUN pip3 install  -r requirement.txt
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
