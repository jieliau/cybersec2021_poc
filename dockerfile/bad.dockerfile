FROM ubuntu:latest

ADD ./iamgood.sh /bin/executeme
RUN chmod +x /bin/executeme &&\
	apt-get update &&\
	apt-get install ncat -y
