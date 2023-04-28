FROM python:3

WORKDIR /insertion

RUN pip3 install pika && \
    pip3 install MarkupSafe==2.0.0 && \
    pip3 install certifi && \
    pip3 install itsdangerous==2.0.1 && \
    pip3 install Jinja2==3.0.3 && \
    pip3 install MarkupSafe==2.0.1 && \
    pip3 install Flask==2.0.2 && \
    pip3 install Flask-PyMongo==2.3.0

COPY . /insertion

ENTRYPOINT [ "python" ]

CMD [ "insertion.py" ]