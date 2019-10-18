# docker-airflow

This repository contains **Dockerfile** of [apache-airflow](https://github.com/apache/incubator-airflow) for [Docker](https://www.docker.com/), with additional demo pipelines by Alex Galea.

See the [original project](https://github.com/puckel/docker-airflow) for more comprehensive information, README, and issue tracking.

## How to run

Here's how I build and run my container. I may be doing things wrong since I'm just getting started with docker.

Below we show code for sqlite SequentialOperator. Once those are running, make sure to test the postgres LocalExecutor scripts as well, since sqlite does not allow for multiprocessing in airflow like postgres does.

Just in case that wasn't clear enough, *do not use SequentialOperator* in production.

### Build image with `docker` then run with `docker-compose`

```
# Build it
docker build . -t airflow_test
docker image ls

# Run it
docker-compose -f docker-compose-sqlite-from-image.yaml up
docker image ls
```

### Build and run with `docker-compose`

```
# Build and run from scratch
docker-compose -f docker-compose.yaml up

# Update production container
# (will stop and restart it)
docker-compose -f docker-compose-sqlite.yaml build
docker-compose -f docker-compose-sqlite.yaml up
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

### Postgres

Run the same commands as above but use `docker-compose-postgres.yaml` instead. Note the differences such as the lack of separate services for the webserver and the scheduler.

```
# Build and run from scratch
docker-compose -f docker-compose-postgres.yaml up

# Query db
docker ps
docker exec -it <ID> psql -U airflow
select * from dag_run;
```



