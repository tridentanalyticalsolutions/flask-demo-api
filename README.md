# FlaskDemo
This is flask api for demo purpose using mongodb


# Getting Started
Below are the instruction how you can clone this repo and set up this demo project on your local machine up and running using docker

# Prerequisites
You have docker installed on your system

# Installing
A step by step guide will help you to install the project using docker

- Clone this repo on your system
- Go into the project root directory
- open terminal in your project root path
- write "docker-compose up" command in terminal and hit enter 

```
docker-compose up
```
  > NOTE : in linux you have to install docker-compose follow this link for installation [Follow link](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/)


# Running the project
 > open the web browser and hit http://localhost:5000/V1/ to verify everything is working or not

# Api endpoints
- /users POST (post as raw json object)
  name
  username
  password
  * Post this data as json object ex {"name":"name","username":"username","password":"password"}

- /users GET (to get all users)  

> ex endpoint http://localhost:5000/V1/users /GET

# Folder structure ofproject: 
.
+-- api
|   +-- static
|   +-- templates
|   +-- init.py
|   +-- config.py
|   +-- user.py
+-- db
|   +-- Dockerfile
+-- server.py
+-- requirement.txt
+-- Dockerfile
+-- docker-compose.yml