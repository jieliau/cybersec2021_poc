FROM ubuntu:latest

RUN groupadd -g 999 mygrp &&\
	useradd -r -u 999 -g mygrp myuser

USER myuser
