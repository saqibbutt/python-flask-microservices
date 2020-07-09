## Running application in docker containers:
#### Using Docker CLI

```
docker network create --driver bridge micro_network (skip if already created)
docker build -t user-srv .
docker run -p 5001:5001 --detach --name user-service --net=micro_network user-srv
```

## Using 'flask shell' to access flask application
```
$ flask shell
from application.models import User
from application import db
admin = User(username="foo", email="foo@admin.com",first_name="foo", last_name="bar", password="admin2020",is_admin=True)
db.session.add(admin)
db.session.commit()
```