FROM python:3.5-alpine
ARG DATABASE_NAME
ARG MLAB_MONGO_URI
ARG MLAB_ZOOKEEPER_URI
ARG WORKER_INSTANCES
ARG LDAP_URI

ENV application_path /opt/dashboard_server
ENV PYTHONPATH ${application_path}:/opt
WORKDIR ${application_path}

COPY . .

RUN python setup.py install
EXPOSE 5000

ENTRYPOINT gunicorn -w ${WORKER_INSTANCES:=1} -b 0.0.0.0:5000 app:app
