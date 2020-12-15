# Simple ToDo List API

This is a demo rest API application for simple2do.xyz site
There are for methods around the endpoint /api/v1/task/:
    *GET*    list all tasks
    *POST*   add a new task
    *PATCH*  update the task status
    *DELETE* delete the task

## Run the app

Assume you have docker installed on your machine, run the following commands.

```
docker build . -t api.simple2do.xyz
docker run -e -e TODO_DB_ENGINE=sqlite3 --rm --name test_simple2do -p 8000:8000 api.simple2do.xyz
```

Open another terminal and run
```
docker exec test_simple2do python manage.py migrate
curl http://localhost:8000/api/v1/task/
```

If you can see the curl gives `[]` as the result, than it's setup successully.

More tests
```
curl -XPOST http://localhost:8000/api/v1/task/ -H 'Content-Type:application/json' -d '{"title":"test title"}'

#Assume the above command returns id 1, then you can update or delete it
curl -XPATCH http://localhost:8000/api/v1/task/1/ -H 'Content-Type:application/json' -d '{"is_done":true}'
curl -XDELETE http://localhost:8000/api/v1/task/1/
```


## Production deployment

* Prerequisits

Need docker-compose installed on production machine, check [install compose](https://docs.docker.com/compose/install/)
In short, run this command on linux.

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

I've setup letsencrypt to get https access via nginx, following this article if you like have your free ssl certificate.
[Nginx and Let’s Encrypt with Docker in Less Than 5 Minutes](https://medium.com/@pentacent/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)


Currently, AWS codepipeline is triggered by the commit in AWS codecommit, github commit trigger needs one more step to change the settings.

* Run pipeline and deployment

Change code and commit to the codecommit
Check the status in AWS codepipeline (only has Source and Build stages as Deploy is not fully automated right now)
Wait for the build done 

In api.simple2do.xyz source code folder, install requirements/dev.txt and run
```
pip install -r requirements/dev.txt
fab -H PROD_HOST deploy
```

*NOTE* It's always nice to setup virtualenv for python development, if you haven't, go to here for detail
[Creation of virtual environments](https://docs.python.org/3/library/venv.html)
