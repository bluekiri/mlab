FROM python:3-jessie

RUN mkdir -p /usr/src/app/api_server
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/api_server

RUN pip3 install --no-cache-dir -r api_server/requirements.txt

COPY . /usr/src/app/api_server

EXPOSE 9090

ENTRYPOINT ["python3"]

CMD ["-m", "api_server"]
