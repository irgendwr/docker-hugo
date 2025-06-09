# Hugo Docker image

[![Docker Image Version](https://img.shields.io/docker/v/irgendwr/hugo)](https://hub.docker.com/r/irgendwr/hugo)
[![Docker Image Size](https://img.shields.io/docker/image-size/irgendwr/hugo)](https://hub.docker.com/r/irgendwr/hugo)
[![Docker Pulls](https://img.shields.io/docker/pulls/irgendwr/hugo)](https://hub.docker.com/r/irgendwr/hugo)

This provides a [Docker](https://www.docker.com/) container image for [Hugo](https://github.com/gohugoio/hugo/), an open-source static site generator.

The image is based on Alpine and also includes:

- [Node](https://github.com/nodejs/docker-node)
- [py-pygments](https://github.com/pygments/pygments)
- [minify](https://github.com/tdewolff/minify)
- rsync
- git
- openssh-client

## Build

Set `ENV VERSION` in the Dockerfile.

```bash
docker pull node:alpine
docker build -t irgendwr/hugo:$version .
docker push irgendwr/hugo:$version
```

## Credit

- [@DeinAlptraum](https://github.com/DeinAlptraum/) for the automatic builder via GitHub actions
- [@jguyomard](https://github.com/jguyomard/) for repository this was forked from: [jguyomard/docker-hugo](https://github.com/jguyomard/docker-hugo)
