FROM node:alpine

RUN apk add --no-cache \
    libc6-compat \
    curl \
    git \
    openssh-client \
    rsync \
    py-setuptools \
    py-pygments

RUN rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

ENV VERSION 0.74.3

RUN mkdir -p /usr/local/src \
    && cd /usr/local/src \
    && curl -L https://github.com/gohugoio/hugo/releases/download/v${VERSION}/hugo_extended_${VERSION}_Linux-64bit.tar.gz | tar -xz \
    && mv hugo /usr/local/bin/hugo \
    && curl -L https://bin.equinox.io/c/dhgbqpS8Bvy/minify-stable-linux-amd64.tgz | tar -xz \
    && mv minify /usr/local/bin/

RUN hugo version
