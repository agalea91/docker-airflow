# docker-airflow

This repository contains **Dockerfile** of [apache-airflow](https://github.com/apache/incubator-airflow) for [Docker](https://www.docker.com/), with additional demo pipelines by Alex Galea.

See the [original project](https://github.com/puckel/docker-airflow) for more comprehensive information, README, and issue tracking.

## How to run

Here's how I build and run my container. I may be doing things wrong since I'm just getting started with docker.

### Build image with `docker` then run with `docker-compose`

```
# Build it
docker build . -t airflow_test
docker image ls

# Run it
docker-compose -f docker-compose-from-image.yaml up
docker image ls
```


### Build and run with `docker-compose`

```
# Build and run from scratch
docker-compose -f docker-compose.yaml up

# Update production container
# (will stop and restart it)
docker-compose -f docker-compose.yaml build
docker-compose -f docker-compose.yaml up
```


### Once it's running...
```

# Bash into it
docker ps
docker exec -it <ID> bash

# Open airflow
GET http://localhost:8080

# Shut everything down
docker-compose down
```


