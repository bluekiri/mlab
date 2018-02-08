FROM python:3.5-alpine
ARG DATABASE_NAME
ARG MLAB_MONGO_URI
ARG MLAB_ZOOKEEPER_URI
ARG WORKER_INSTANCES
ARG LDAP_URI
ARG PORT

ENV application_path /opt/dashboard
WORKDIR ${application_path}

COPY . .

RUN pip install .
EXPOSE ${PORT}
ENTRYPOINT gunicorn -t 300 -w ${WORKER_INSTANCES} -b 0.0.0.0:${PORT} dashboard.app:app
