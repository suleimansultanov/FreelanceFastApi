#!/bin/bash
set -e

# Переменные
AWS_ACCOUNT_ID=149292675029
AWS_REGION=us-east-1
ECR_REPOSITORY=freelanceappapi
IMAGE_TAG=latest

# Логинимся в ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Сборка Docker образа под amd64
docker build --platform linux/amd64 -t $ECR_REPOSITORY:$IMAGE_TAG .

# Тегируем образ для ECR
docker tag $ECR_REPOSITORY:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG

# Пушим образ в ECR
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG

echo "Docker image pushed successfully: $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:$IMAGE_TAG"
