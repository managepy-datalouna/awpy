FROM python:3.9.12-slim

ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/usr/local/go/bin

RUN apt-get update && apt-get install -y \
    wget

COPY . /opt/app
WORKDIR /opt/app

RUN wget "https://go.dev/dl/go1.19.1.linux-amd64.tar.gz"
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.19.1.linux-amd64.tar.gz

RUN pip3 install --upgrade pip setuptools \
   && pip3 install --no-cache-dir -r requirements.txt