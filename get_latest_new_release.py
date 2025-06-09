import requests
import os
from base64 import b64encode
import re
from sys import stderr


def make_comparable(version_string: str) -> list[int]:
    return [int(part) for part in version_string.replace("v", "").split(".")]


ENDPOINT_HUGO_IMAGES = "https://ghcr.io/v2/gohugoio/hugo/tags/list"
ENDPOINT_MY_TAGS = (
    "https://api.github.com/repos/DeinAlptraum/docker-hugo/tags?per_page=1"
)

request_counter = 1

# Check the latest release we've done
res = requests.get(ENDPOINT_MY_TAGS)
try:
    latest_tag = res.json()[0]["name"]
    print("Checking for releases older than", latest_tag, file=stderr)
except IndexError:
    latest_tag = "v1.0.0.0"
    print("No tags found, starting with newest Hugo release", file=stderr)


auth = b64encode(os.environ["GH_TOKEN"].encode()).decode()
res = requests.get(ENDPOINT_HUGO_IMAGES, headers={"Authorization": f"Bearer {auth}"})

version_regex = re.compile("v([0-9]+\\.){2}[0-9]+")
releases_to_process = [
    tag
    for tag in res.json()["tags"]
    if version_regex.match(tag) and make_comparable(tag) < make_comparable(latest_tag)
]

print("Found releases:", file=stderr)
print(releases_to_process, file=stderr)

if releases_to_process:
    minimum_new_version = max(releases_to_process, key=make_comparable)
    print("Preparing image for", minimum_new_version, file=stderr)
else:
    minimum_new_version = "NONE"
    print("No new release found, stopping.", file=stderr)

print("version=", minimum_new_version.replace("v", ""), sep="")
