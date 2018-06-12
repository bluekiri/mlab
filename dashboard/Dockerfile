FROM python:3.5-jessie
ARG DATABASE_NAME
ARG MLAB_MONGO_URI
ARG MLAB_ZOOKEEPER_URI
ARG WORKER_INSTANCES
ARG LDAP_URI
ARG PORT

ENV application_path /opt/dashboard
WORKDIR ${application_path}

COPY . .

RUN pip install --process-dependency-links .
RUN apt-get update && \
    apt-get install -y nodejs npm
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN cd src/dashboard && \
    npm install && \
    ./node_modules/bower/bin/bower install --allow-root && \
    ./node_modules/gulp/bin/gulp.js
EXPOSE ${PORT}
ENTRYPOINT gunicorn -t 300 -w ${WORKER_INSTANCES} -b 0.0.0.0:${PORT} dashboard.app:app
