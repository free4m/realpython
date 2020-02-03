FROM python:3.7.5-slim

# setup virtual environment
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# python commands to run
FROM python:3.7.5-slim
WORKDIR /usr/src/app
RUN python -m pip install \
        parse \
        realpython-reader
COPY headlines.py .
CMD ["python", "headlines.py"]