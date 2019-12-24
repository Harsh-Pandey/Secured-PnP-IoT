FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install mosquitto -v
RUN pip3 install  -r requirement.txt
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
