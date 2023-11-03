
# TODO app

This project was built using [Django](https://docs.djangoproject.com/) Framework. It covers basic CRUD operations to handle making, editing, and deleting todo items.

## Installation
This project was containerized using Docker. You need to install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) first in your local setup.

## How to run
1. Build your project
```
docker-compose build
```

2. Run your project
```
docker-compose up
```

3. Database Migration
```
docker exec -ti todo_web_1 python manage.py migrate
```

4. Check running containers
```
docker ps
```

5. Check logs
```
docker logs -f --tail 100 todo_web_1
```

6. Stop your project
```
docker-compose stop
```


### Resources
- Python
    - [30 days of python](https://github.com/Asabeneh/30-Days-Of-Python/tree/master)
    - [How to get started with python](https://www.programiz.com/python-programming/first-program)
- Django
    - [Django ebooks](https://www.javatpoint.com/best-books-to-learn-django-for-beginners-and-advance-programmers)