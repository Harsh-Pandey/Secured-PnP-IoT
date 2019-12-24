#Arguments passed to this script amd/arm,hardware raspi/laptop mqtt/amqp/rabbitmq
#"arm", "raspi", "stretch","mqtt"
#sudo apt-get remove docker docker-engine docker.io containerd runc  
#sudo apt-get update
#sudo apt-get install \apt-transport-https \ca-certificates \curl \gnupg-agent \Software-properties-common
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#sudo apt-key fingerprint 0EBFCD88
if [[ $1 -eq "amd" ]];
then
	#sudo add-apt-repository \"deb [arch=amd64] https://download.docker.com/linux/ubuntu \$(lsb_release -cs) \stable"
elif [[ $1 -eq "arm" ]]
	#sudo add-apt-repository \"deb [arch=armhf] https://download.docker.com/linux/ubuntu \$(lsb_release -cs) \stable"
fi
#sudo apt-get update
#sudo apt-get install docker-ce docker-ce-cli containerd.io
if [[ $4 -eq "mqtt" ]];then
	if [[ $3 -eq "stretch" ]];
	then
		dockerfile=./mqtt/stretch/

	elif [[ $3 -eq "buster" ]];
	then
		dockerfile=./mqtt/buster/
	elif [[ $3 -eq "ubuntu" ]]
	then
		dockerfile=./mqtt/ubuntu/
#docker build -t iot:1.0.0 $dockerfile
