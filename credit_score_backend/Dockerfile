FROM python:3.12.3-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get -y --no-install-recommends install \
    libgomp1

COPY . /usr/src/app

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["-m", "server"]