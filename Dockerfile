FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -ms /bin/bash user

# dependencies
RUN apt-get update && \
    apt-get install -y iputils-ping \
    && apt-get install -y default-libmysqlclient-dev build-essential \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir /project_test 
WORKDIR /project_test

COPY requirements/requirements.txt /project_test/
RUN pip install --upgrade pip==23.0.1

RUN pip install -r requirements.txt

# Copy nginx configuration file
# COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8000

# Run it
COPY . /project_test/

CMD ["python3", "project_test/manage.py", "runserver", "0.0.0.0:8000"]
