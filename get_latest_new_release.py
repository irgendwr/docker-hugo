import requests
import os
from base64 import b64encode
import re
from sys import stderr


def make_comparable(version_string: str) -> list[int]:
    return [int(part) for part in version_string.replace("v", "").split(".")]


ENDPOINT_HUGO_IMAGES = "https://ghcr.io/v2/gohugoio/hugo/tags/list"
ENDPOINT_OUR_TAGS = (
    "https://hub.docker.com/v2/namespaces/nightoo/repositories/hugo/tags"
)

version_regex = re.compile("([0-9]+\\.){2}[0-9]+")
our_tags = set()
try_next_page = True
current_url = ENDPOINT_OUR_TAGS
while try_next_page:
    print("Retrieving tags at", current_url, file=stderr)
    content = requests.get(current_url).json()
    our_tags = our_tags.union(
        [
            image["name"]
            for image in content["results"]
            if version_regex.match(image["name"])
        ]
    )

    current_url = content["next"]
    try_next_page = bool(current_url)

auth = b64encode(os.environ["GH_TOKEN"].encode()).decode()
res = requests.get(ENDPOINT_HUGO_IMAGES, headers={"Authorization": f"Bearer {auth}"})

available_tags = set(
    [tag[1:] for tag in res.json()["tags"] if version_regex.match(tag)]
)
tags_to_process = available_tags - our_tags

print("Unprocessed releases:", file=stderr)
print(tags_to_process, file=stderr)

if tags_to_process:
    maximum_new_version = max(tags_to_process, key=make_comparable)
    print("Preparing image for", maximum_new_version, file=stderr)
else:
    maximum_new_version = "NONE"
    print("No new release found, stopping.", file=stderr)

print(f"version={maximum_new_version}")
