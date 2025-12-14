from bs4 import BeautifulSoup
import re
import requests

url = r"https://simplegreensoul.com/top-13-asian-fruits-you-should-know-about-try"

def get_data(url):

    resp = requests.get(url, verify=False)
    soup = BeautifulSoup(resp.text, "html.parser")

    # match headings like "1. Something", "2. Something else"
    numbered_heading_pattern = re.compile(r"^\d+\.\s+")

    outputs = []

    # find all headings
    headings = soup.find_all(["h2", "h3"])

    for i, heading in enumerate(headings):
        title_text = heading.get_text(strip=True)

        # skip non-numbered headings
        if not numbered_heading_pattern.match(title_text):
            continue

        image_urls = []

        # walk forward until next numbered heading or end
        next_node = heading.next_sibling

        while next_node:
            # stop if we hit another numbered heading
            if (
                getattr(next_node, "name", None) in ["h2", "h3"]
                and numbered_heading_pattern.match(
                    next_node.get_text(strip=True)
                )
            ):
                break

            # collect images
            if getattr(next_node, "name", None):
                imgs = next_node.find_all("img")
                for img in imgs:
                    src = img.get("src")
                    if src:
                        image_urls.append(src)

            next_node = next_node.next_sibling

        outputs.append({
            "title": title_text,
            "image_urls": image_urls
        })
    return outputs

def print_csv(outputs):
    for section in outputs:
        fruit = section["title"]
        image_urls = section.get("image_urls", [])
        print(f"{fruit[3:]}, {image_urls[0]}")