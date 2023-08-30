# Project requirements 
- Development: Python 3, docker & docker-compose
- Deployment: docker, aws cli, kustomize

### Building from source
```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```
### Configuration
The app reads the db connection url from the env variable `DATABASE_URL`. Default value `postgres://postgres:postgres@db:5432/db`
### Run tests
`python -m unittest discover`
### Running the app locally
```
docker-compose up -d
```
Once docker-compose is running, code changes will be automatically reloaded without needing to restart the container.
App rest api will be exposed in `http://localhost:8000`
#### Example queries
```
curl -X PUT localhost:8000/hello/marcos -d '{"dateOfBirth":"2020-08-31"}' -H 'Content-Type: application/json'
```
```
curl http://localhost:8000/hello/marcos
```
Data will be stored in a postgresDB.
### Kubernetes deployment
Secret has to be stored in aws secrets manager with the id <ENV>_DATABASE_URL
It builds & pushes the docker image, generates the k8s manifest (secrets, deployment with 3 replicas, service, ingress to expose the service)
Deployed with kubectl with default strategy, rolling deployment that replaces the replicas one by one without downtime.
```
./k8s_deploy.sh <ENVIRONMENT>
````

### CircleCI pipeline
Runs tests, does the build, push and k8s deployment. By default it deploys feature branches in dev env and master & hotfix branches to staging and after approval in production.
### Proposed infrastructure
Attached pdf: [Proposed Infrastructure](Proposed_infra.pdf)