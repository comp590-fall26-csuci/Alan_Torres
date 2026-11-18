FROM debian:stable-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY Makefile ./
COPY main.c fibonacci.c test_fibonacci.c ./
COPY headers/ ./headers/

RUN make fibonacci fibonacci_tests

CMD ["make", "test"]