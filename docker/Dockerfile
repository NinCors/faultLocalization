
FROM openjdk:7

MAINTAINER Rui Abreu <rui@computer.org>

RUN apt-get update && \
  apt-get -y install git wget gzip unzip ant

RUN \
  mkdir fl && \
  cd fl && \
  git clone https://rma@bitbucket.org/rjust/fault-localization-data.git && \
  cd fault-localization-data && \
  ./setup.sh && \
  . ~/.bashrc

