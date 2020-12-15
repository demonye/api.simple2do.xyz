FROM python:3.8-alpine

ARG APP_DIR=/app/todo_list/

WORKDIR ${APP_DIR}

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY requirements/base.txt requirements/prod.txt ${APP_DIR}
RUN pip install -r prod.txt && rm base.txt prod.txt

COPY src .

CMD ["gunicorn", "todo_list.wsgi", "-b", ":8000", "-w", "2"]
