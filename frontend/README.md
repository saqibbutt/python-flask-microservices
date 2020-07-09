## Running application in docker containers:
#### Using Docker CLI
```
docker network ls
docker network create --driver bridge micro_network (skip if already created)
docker build -t frontend-srv .
docker run -p 5000:5000 --detach --name frontend-service --net=micro_network frontend-srv
```