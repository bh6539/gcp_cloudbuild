FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "web/manage.py", "runserver", "0.0.0.0:8000"]