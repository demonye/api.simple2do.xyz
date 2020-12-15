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
