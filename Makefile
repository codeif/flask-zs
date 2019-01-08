build:
	docker build -t zs-example .

init-db:
	docker-compose exec web pipenv run flask init-db
