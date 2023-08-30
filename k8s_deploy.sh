#!/usr/bin/env bash
set -e

[ -z "$1" ] && { echo 'No Environment supplied.'; exit 1; } || ENVIRONMENT="$1"


# Get secrets from AWS secret manager
echo 'DATABASE_URL=$(aws secretsmanager get-secret-value --secret-id "{$ENVIRONMENT}_DATABASE_URL" --region eu-central-1 --query SecretString --output text)'


# Build/push Docker image
DOCKER_TAG="$(date -u +"%Y%m%d%H%M%S")"
REPO_HOST="myrepo.dkr.ecr.eu-central-1.amazonaws.com"
echo 'aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin "$REPO_HOST"'
DOCKER_IMAGE="$REPO_HOST/my-app:$DOCKER_TAG"
echo docker build -f Dockerfile -t "$DOCKER_IMAGE" . --platform=linux/amd64
echo docker push "$DOCKER_IMAGE"

# Prepare kubernetes manifests & apply
pushd kustomization

echo "DATABASE_URL=secret_from_aws" > application.properties
echo "get .kubeconfig from secrets manager"

kustomize edit set image $DOCKER_IMAGE
echo "kubectl config use-context $ENVIRONMENT"
kustomize build #| kubectl apply -f -

popd