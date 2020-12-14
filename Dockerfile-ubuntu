FROM python:3.8

ARG APP_DIR=/app/todo_list/

WORKDIR ${APP_DIR}

COPY requirements/base.txt requirements/prod.txt ${APP_DIR}
RUN pip install -r prod.txt && rm base.txt prod.txt

RUN groupadd -r todo_list && useradd -u 1000 --no-log-init -r -g todo_list todo_list
RUN chown -R todo_list:todo_list ${APP_DIR}
USER todo_list
COPY src .

CMD ["gunicorn", "todo_list.wsgi", "-b", ":8000", "-w", "2"]
