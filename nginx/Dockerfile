FROM nginx

RUN echo 'deb http://deb.debian.org/debian stretch-backports main' >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install certbot python-certbot-nginx -t stretch-backports -y