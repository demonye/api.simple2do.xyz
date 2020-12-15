import boto3
from fabric import task


@task
def deploy(cli):
    key_id = input('AWS access key id? ')
    key = input('AWS secret access key? ')
    region = input('AWS default region? ')
    registry = input('ECR registry (without your repo name)? ')
    scm_id = input('SCM secret_id for db? ')
    cli.run('mkdir -p ~/.simple2do/nginx/conf.d')
    cli.run('mkdir -p ~/.simple2do/nginx/data/certbot')

    cli.put('env_file', '.simple2do')
    cli.run(f'echo AWS_ACCESS_KEY_ID={key_id} >> .simple2do/env_file')
    cli.run(f'echo AWS_SECRET_ACCESS_KEY={key} >> .simple2do/env_file')
    cli.run(f'echo AWS_DEFAULT_REGION={region} >> .simple2do/env_file')
    cli.run(f'echo TODO_SCM_SECRET_ID={scm_id} >> .simple2do/env_file')

    cli.put('nginx/conf.d/default.conf', '.simple2do/nginx/conf.d')
    cli.put('docker-compose.yml', '.')
    cli.run(f'export DOCKER_REGISTRY={registry}')
    cli.run('docker-compose stop web && docker-compose up -d')
    cli.run('rm ./docker-compose.yml ~/.simple2do/env_file')
