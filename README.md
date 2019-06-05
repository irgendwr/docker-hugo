# Hugo Docker Image

[![Docker Automated build](https://img.shields.io/docker/automated/irgendwr/hugo.svg)](https://store.docker.com/community/images/irgendwr/hugo)
[![Docker Build Status](https://img.shields.io/docker/build/irgendwr/hugo.svg)](https://store.docker.com/community/images/irgendwr/hugo/builds)
[![Docker Pulls](https://img.shields.io/docker/pulls/irgendwr/hugo.svg)](https://store.docker.com/community/images/irgendwr/hugo)
[![Image Info](https://images.microbadger.com/badges/image/irgendwr/hugo.svg)](https://microbadger.com/images/irgendwr/hugo)

This is a fork from [jguyomard/docker-hugo](https://github.com/jguyomard/docker-hugo) that adds [Node](https://github.com/nodejs/docker-node) and py-pygments.

[Hugo](https://github.com/gohugoio/hugo/) is a fast and flexible static site generator, written in Go.
Hugo flexibly works with many formats and is ideal for blogs, docs, portfolios and much more.
Hugo’s speed fosters creativity and makes building a website fun again.

This Lightweight Docker Image is based on Alpine, and comes with rsync for Continuous Deployment.

This Docker image also comes with:

- [Node](https://github.com/nodejs/docker-node)
- rsync
- git
- openssh-client
- [minify](https://github.com/tdewolff/minify)
- py-pygments
