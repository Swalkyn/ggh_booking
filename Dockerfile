FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y sudo build-essential curl python3 python3-pip python3-dev

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD ["make", "setup"]