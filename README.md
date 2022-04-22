# ecs-project-1

ECS test

## Steps

1. Create ECR Repository
2. Create Cloud9/VSCode environment
3. Create Docker image
4. Authenticate ECR registry
    `aws ecr get-login-password --region <Region-Code> | docker login --username AWS --password-stdin <Account-Number>.dkr.ecr.<Region-Code>.amazonaws.com`
5. Build the image
    `docker build -t fazliecsrepo .`
