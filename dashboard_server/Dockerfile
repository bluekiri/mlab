FROM python:3.5-alpine
ARG DATABASE_NAME
ARG MLAB_MONGO_URI
ARG MLAB_ZOOKEEPER_URI
ARG WORKER_INSTANCES
ARG LDAP_URI
ARG SERVICE_PORT

ENV application_path /opt/dashboard_server
WORKDIR ${application_path}

COPY . .

RUN pip install .
EXPOSE 5000
ENTRYPOINT gunicorn -t 300 -b 0.0.0.0:5000 -w ${WORKER_INSTANCES} dashboard_server.app:app
