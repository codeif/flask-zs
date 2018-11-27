FROM kennethreitz/pipenv
# FROM example_app

COPY . /app
WORKDIR /app

RUN pipenv sync

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0"]