FROM python:3-jessie
ENV application_path=/opt/api_server

RUN mkdir -p application_path
WORKDIR application_path

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt