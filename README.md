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
docker run --env_file /tmp/simple2do_env_file
```
