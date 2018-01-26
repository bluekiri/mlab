FROM ubuntu:16.04
ENV application_path /opt/dashboard_server
ENV PYTHONPATH ${application_path}:/opt
WORKDIR ${application_path}

COPY . .
RUN bash setup.sh
EXPOSE 5000

ENTRYPOINT gunicorn -w ${DASHBOARD_WORKERS:=1} -b 0.0.0.0:5000 app:app
