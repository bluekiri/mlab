FROM ubuntu:16.04
ENV application_path /opt/api_servers
ENV PYTHONPATH ${application_path}:/opt

WORKDIR ${application_path}

COPY . .
RUN bash setup.sh
EXPOSE 9090

ENTRYPOINT echo ${WORKER_INSTANCES:=3} && gunicorn --config application/conf/gunicorn.conf.py -w ${WORKER_INSTANCES} -b 0.0.0.0:9090 application.app:api