# mini 5G Core for Network Slicing

## Dependencies
* docker https://docs.docker.com/engine/install/ubuntu/
* docker-compose https://docs.docker.com/compose/install/
* python 3.9

## How to run?

```
docker-compose build  # build
docker-compose up  # run
docker-compose up --build # build&run in one step
```

or with -d flag in detached (non-blocking) mode
```
docker-compose up --build -d
docker-compose stop  # stop containers
```

## How to develop
Highest level modules are the Network Function (NF) which run in separate containers.
* each NF is a web server that exposes API and is available on internal (docker) and external (host) network via ports defined in docker-compose.yml
* each NF must have Dockerfile, requirements file and service implementation
* if new service is added then docker-compose must be updated

Openapi file contains definition of the service API and **must** be consistent with the routes definition (https://connexion.readthedocs.io/en/latest/routing.html - RestyResolver section) i.e.
* path definition represents the module that implements it e.g. /users -> {RestyResolver_MAIN_DIR (check app.py)}/users.py:{method}, where method represents HTTP method and is mapped to python in following way GET->search or get, PUT->put, POST->post or DELETE->delete


Sample curl to one of the containers:
```
export amf=localhost:5000
curl -XPUT http://${amf}/flows -d @flow.json -H "Content-Type: application/json"

where flow.json
{
  "srcIp": "100.0.0.1",
  "dstIp": "200.0.0.1"
}

```