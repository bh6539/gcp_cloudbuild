FROM python:3.6-slim

WORKDIR /app

COPY requirements.txt ./
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "web/manage.py", "runserver", "0.0.0.0:8000" ]