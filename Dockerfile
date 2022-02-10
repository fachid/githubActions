FROM jenkins/jenkins:2.321
# if we want to install via apt
USER root

RUN apt-get update -yqq \
    && apt-get upgrade -yqq


USER jenkins
