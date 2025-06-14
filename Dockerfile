FROM ghcr.io/gohugoio/hugo:v0.147.4

USER root:root

RUN apk add --no-cache \
    libc6-compat \
    curl \
    git \
    openssh-client \
    rsync \
    py-setuptools \
    py-pygments

RUN rm -rf /tmp/* /var/tmp/*

RUN mkdir -p /usr/local/src \
    && cd /usr/local/src \
    && curl -L https://github.com/tdewolff/minify/releases/latest/download/minify_linux_amd64.tar.gz | tar -xz \
    && mv minify /usr/local/bin/

USER hugo:hugo

RUN hugo version && minify --version && echo -e "node \c" && node --version
