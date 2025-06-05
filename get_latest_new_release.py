import requests

def make_comparable(version_string: str) -> list[int]:
    return [int(part) for part in version_string.replace("v", "").split(".")]

ENDPOINT_HUGO_RELEASES = "https://api.github.com/repos/gohugoio/hugo/releases"
ENDPOINT_MY_TAGS = "https://api.github.com/repos/DeinAlptraum/docker-hugo/tags?per_page=1"

request_counter = 1

# Check the latest release we've done
res = requests.get(ENDPOINT_MY_TAGS)
try:
    latest_tag = res.json()[0]["name"]
except IndexError:
    latest_tag = "v0.88.1"
print("Checking for releases younger than", latest_tag)

releases_to_process = []
try_next_page = True
current_url = ENDPOINT_HUGO_RELEASES
while try_next_page:
    print("Retrieving releases at", current_url)
    if request_counter < 10:
        res = requests.get(current_url)
    else:
        print("Reached 10 requests")
        exit(1)
    request_counter += 1
    content = res.json()
    for release in content:
        # Only check next page if the last release was still newer than our latest
        try_next_page = False
        if make_comparable(latest_tag) < make_comparable(release["name"]):
            try_next_page = True
            # Remove the "v" at the start of the tag name
            releases_to_process.append(release["name"][1:])
        
    if try_next_page:
        # Retrieve link to next page from Link header
        pagination_urls = res.headers["Link"]
        for element in pagination_urls.split(","):
            if 'rel="next"' in element:
                current_url = element.split(">")[0].split("<")[1]
                break

print("Found releases:")
print(releases_to_process)

if releases_to_process:
    minimum_new_version = min(releases_to_process, key=make_comparable)
    print("Preparing image for", minimum_new_version)
else:
    minimum_new_version = "NONE"
    print("No new release found, stopping.")

with open("_version.txt", "w") as f:
    f.write(minimum_new_version)

