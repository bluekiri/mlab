FROM python:3.5-alpine
ARG DATABASE_NAME
ARG MLAB_MONGO_URI
ARG MLAB_ZOOKEEPER_URI
ARG WORKER_INSTANCES
ARG PORT

ENV application_path /opt/worker
WORKDIR ${application_path}

COPY . .

RUN pip install .

EXPOSE ${PORT}
ENTRYPOINT gunicorn -b 0.0.0.0:${PORT} -w ${WORKER_INSTANCES} --config=python:worker.application.conf.gunicorn_conf worker.app:app
