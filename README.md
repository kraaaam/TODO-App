
# TODO app

This project was built using [Django](https://docs.djangoproject.com/) Framework. It covers basic CRUD operations to handle making, editing, and deleting todo items.

## Installation
This project was containerized using Docker. You need to install [Docker](https://docs.docker.com/get-docker/) and [Docker ](https://docs.docker.com/compose/install/) first in your local setup.

## How to run
1. Build your project
```
docker-compose build
```

2. Run your project
```
docker-compose up
```

3. Check running containers
```
docker ps
```

4. Check logs
```
docker logs -f --tail 100 todo_web_1
```