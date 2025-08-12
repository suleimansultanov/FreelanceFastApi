#!/bin/bash

set -e

echo "📄 Создаём trust policy..."
cat <<EOF > ecs-trust-policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

echo "🔧 Создаём роль ecsTaskExecutionRole..."
aws iam create-role \
  --role-name ecsTaskExecutionRole \
  --assume-role-policy-document file://ecs-trust-policy.json

echo "🔐 Прикрепляем политику AmazonECSTaskExecutionRolePolicy..."
aws iam attach-role-policy \
  --role-name ecsTaskExecutionRole \
  --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy

echo "🧼 Удаляем временный файл..."
rm ecs-trust-policy.json

echo "✅ Готово! Роль ecsTaskExecutionRole успешно создана и настроена."
