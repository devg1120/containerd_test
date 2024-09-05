FROM ubuntu
#MAINTAINER Foo Bar foo@example.jp
#ENV http_proxy="http://10.190.31.15:8080/"
#ENV https_proxy="https://10.190.31.15:8080/"
RUN apt-get update
RUN apt-get install -y nginx
                        # nginx version: nginx/1.24.0 (Ubuntu)




#ADD ./conf/default.conf /etc/nginx/sites-available/default
#ADD ./html /var/www/html

COPY ./conf/default.conf /etc/nginx/sites-available/default
COPY ./html/ /var/www/html/

ENTRYPOINT /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf

