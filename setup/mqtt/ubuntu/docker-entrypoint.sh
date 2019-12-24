#!/bin/bash

set -e 

# start avahi-mosqutto
mosquitto -c /etc/mosquitto/mosquitto.conf & > /dev/null
# While running docker run  arguments can be passed so execute that
if [ $# -gt 0 ]
then
	echo -en "Executing : $@\n"
	$@
fi

