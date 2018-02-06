FROM python:3.5-alpine
ARG DATABASE_NAME
ARG MLAB_MONGO_URI
ARG MLAB_ZOOKEEPER_URI
ARG WORKER_INSTANCES
ARG SERVICE_PORT

ENV application_path /opt/api_servers
WORKDIR ${application_path}

COPY . .

RUN pip install .

EXPOSE 9090
ENTRYPOINT gunicorn -b 0.0.0.0:9090 -w ${WORKER_INSTANCES} --config=python:api_servers.application.conf.config api_servers.app:app
