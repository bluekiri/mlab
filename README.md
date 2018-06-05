# MLAB framework

## Overview
Mlab is a framework who help us to manage machine learning projects in a production environment.
Full documentation about web service is deployed by swagger.

Also you can run a docker container to release the application.

Testing is integrated with Tox framework.

## Table of content
[TOC]

## Architecture seen from afar
![alt text](var/asserts/MLlab-UI-architecture.png)


## Requirements
Python 3.5


## How it works
Is pretty simple, this project run a number of workers for a specific host, and also a dashboard as orchestator.  
Ok, but what is a worker? One worker instance is as simple as webservice, who main goal is load machine learning models in memory in a transparent manner for their consumers.

The orchestrator is in charge of controlling the workers machine learning algorithm loaded trough the dashboard.  
 

## Dashboard Orchestrator

### Requirements
```
sudo apt-get install -y gfortran python3-pip virtualenvwrapper supervisor libatlas-dev libatlas3gf-base python3-scipy python3-numpy
```
### Initial configuration
```
TODO
```
### Usage
```
TODO
```
To run the server, please execute the following from the root directory.  
If you like run a unique server instance (for example for local development), run it:
```
python3 -m dashboard_server
```
else if you want to deploy run it (Login as sudo user):

```
TODO run as a service
```
and open your browser to here:

```
http://localhost:5000/hbp_dashboard
```

### Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t hbp_dashboard dashboard_server

# starting up a container
docker run -p 5000:5000 hbp_dashboard
```

### Testing
To launch the integration tests, use tox:
```
sudo pip install tox
tox
```


## Workers
This example uses the [Connexion] library on top of Flask.
### Initial configuration
```
TODO
```

### Usage

```
sudo su - hbp_api_server
```
To run the server, please execute the following from the root directory:
All as you need to code to run the workers is on api_server folder.
```
TODO run as a service...
```
and open your browser to here:

```
http://localhost:9090/v1/ui/
```