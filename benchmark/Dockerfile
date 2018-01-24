FROM python:3.5-alpine
ENV application_path /opt/api_servers
ENV PYTHONPATH ${application_path}:/opt

WORKDIR ${application_path}

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 9090

ENTRYPOINT echo ${WORKER_INSTANCES:=3} && gunicorn --config application/conf/gunicorn.conf.py -w ${WORKER_INSTANCES} -b 0.0.0.0:9090 application.app:api