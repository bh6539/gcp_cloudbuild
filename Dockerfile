FROM python:3

WORKDIR .

COPY requirements.txt ./
COPY ./djconfig ./djconfig

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-summernote
CMD [ "python3", "djconfig/manage.py", "runserver", "0.0.0.0:8000" ]
