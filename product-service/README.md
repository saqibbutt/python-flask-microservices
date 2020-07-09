## Running application in docker containers:
#### Using Docker CLI
```
docker network ls
docker network create --driver bridge micro_network (skip if already created)
docker build -t product-srv .
docker run -p 5002:5002 --detach --name product-service --net=micro_network product-srv
```