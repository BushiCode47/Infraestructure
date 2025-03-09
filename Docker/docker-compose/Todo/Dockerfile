FROM python:3.9.21-alpine3.21

WORKDIR /app

COPY /src .

RUN pip install psycopg2-binary flask flask_sqlalchemy

EXPOSE 5000

CMD [ "python", "todo.py" ]