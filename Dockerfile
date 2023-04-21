FROM python:3.6-slim

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "web/manage.py", "runserver", "0.0.0.0:5000"]