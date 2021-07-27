# GraphQL example using strawbeey

## Как запустить
Run
~~~~
$ make build
~~~~
~~~~
$ make compose-start
~~~~
## Запуск тестов
~~~~
$ docker-compose exec -e TEST=True app pytest -x -vv
~~~~
## GraphQL
Интерактивная оболочка доступна по адресу:
~~~
http://127.0.0.1:8000/graphql
~~~
