FROM library/python:3.6-stretch
RUN pip3 install pika
WORKDIR /healthcheck
COPY . /healthcheck
ENTRYPOINT [ "python3" ]
CMD [ "healthcheck.py" ]