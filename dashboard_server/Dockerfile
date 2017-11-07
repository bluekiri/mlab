FROM python:3.5-alpine
ENV application_path /opt/dashboard_server
ENV PYTHONPATH ${application_path}:/opt
WORKDIR ${application_path}

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000

ENTRYPOINT  ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "application.app:app"]