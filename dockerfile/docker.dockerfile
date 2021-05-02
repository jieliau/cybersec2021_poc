FROM ubuntu:latest

RUN apt-get update &&\
	apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y &&\
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg &&\
	echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null &&\
	apt-get update &&\
	apt-get install docker-ce-cli -y

