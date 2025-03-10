FROM python:3.9.21-alpine3.21

WORKDIR /app

COPY /src .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "todo.py" ]