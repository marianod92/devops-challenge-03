# devops-challenge-03

- Run app via flask
```
export APP_SETTINGS="config.ProductionConfig" | flask run --host=0.0.0.0 --port=5001
```

- Build Docker Image (with custom tag name)

````
docker build -t test:1 .
````

- Docker-compose

```
docker-compose down; docker-compose up --build --remove-orphans

```