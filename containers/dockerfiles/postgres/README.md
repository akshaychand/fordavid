#SQL Initialization

This image builds on top of Postgres:alpine image from Dockerhub. For more details, check out 
[this link.]((https://hub.docker.com/_/postgres/))


To enhance the base image, specify *.sh or *.sql scripts in the "initsql" folder to inject startup SQL scripts that 
should be executed when the image is first built. Check out the "How to extend this image" section in the above article 
for more details. 