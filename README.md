# MessageBoardApp2
Simple web application that prints messages stored in the posts DB table to a webpage.
Use URL:  http://localhost:8000/ if you decide to run the MessageBoardApp using 
the built-in django sqlite3 webserver.  (python manage.py runserver)

This application can be run in a docker container. It can be deployed and run in a kubernetes cluster as well.  Instructions to run the app in a kubernetes cluster are located in the documentation folder. 

The app can be containerized using Dockerfile and docker-compose.yml.  User the -f option if your docker-compose file has a different name than the default one.

The MessageBoardApp uses Postgres11 DB to store message in the posts DB table and uses nginx to 
serve the home page that displays messages previously entered.  To post new messages to the message
board use the admin application at  http://localhost:8000/admin.  The admin page allows you to
save/update/delete post messages.  

Build a docker container image and run it using the command:
docker-compose up -d --build

To build and run the docker-compose image, you must install 

1. Docker engine.  For centos, use this link:  https://docs.docker.com/engine/install/centos/

2. Install docker-compose with the command: sudo pip install docker-compose

3. CD to the MessageBoardApp top directory where manage.py is located and run the command to 
build and run the docker-compose image: 

docker-compose up -d --build 

Since the docker-compose.yml file exposes the nginx port 1338:80, access the MessageBoardApp at:
http://localhost:1338/

Access the admin app to enter messages and save them to the Postgres DB at:
http://localhost:1338/admin

The admin app allows use to create messages to post.  Messages are saved in the postgres database.

To build and run the MessageBoardApp using the docker unofficial/public images login into Dockerhub (https://hub.docker.com/) and download the web image
from the repository:

1. monicamarshall/messageboardproject_web

You can also open a terminal on your linux box, login into dockerhub using the command: docker login -u <username>, enter you password,
Then issue the docker pull command to download the MessageBoarddApp image.  Then use the command:  docker-compose up
to run the image:

1. docker pull monicamarshall/messageboardproject_web:v1.0
2. docker-compose up -d --build

The document dockerComposeDockerStack deployment guides you through the deployment of the application to Docker and to Kubernetes.
