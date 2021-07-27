build:
	docker build --force-rm $(options) -t films:latest .

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)
