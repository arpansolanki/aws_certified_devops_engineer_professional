#!/bin/bash
yum install httpd -y
service httpd start
echo "<html><body><h1>Hello from Server<h1></body></html>" > /var/www/html/index.html