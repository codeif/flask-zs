build:
	docker build -t zs-example .

shell:
	docker-compose exec web /bin/bash

init-db:
	docker-compose exec web pipenv run flask init-db
