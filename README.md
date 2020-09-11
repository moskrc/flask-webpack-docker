### Installation

```Bash
# dev
$ cp .env.dev.sample .env.dev
$ docker-compose up --build
# prod
$ cp .env.prod.sample .env.prod
$ docker-compose -f docker-compose.prod.yml up --build
$ docker exec -ti app ./manage.py recreate_db
```

