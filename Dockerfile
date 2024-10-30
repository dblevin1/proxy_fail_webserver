FROM python:3.10-slim-buster

WORKDIR /app

COPY . .
RUN pip install .

EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
