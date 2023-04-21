FROM python:3

WORKDIR .

COPY requirements.txt ./
COPY ./web ./web

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "djconfig/manage.py", "runserver", "0.0.0.0:8000" ]
