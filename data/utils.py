import requests
from bs4 import BeautifulSoup

BASE_URL: str = "https://theamazingworldofgumball.fandom.com/wiki"

USER_AGENT: dict[str, str] = {
    "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
                   "AppleWebKit/537.36 (KHTML, like Gecko)"
                   "Chrome/45.0.2454.101 Safari/537.36"),
    "referer":
    BASE_URL
}

rs = requests.Session()


class Status:

    @staticmethod
    def error(msg: str) -> None:
        print(f"[ERROR] {msg}")

    @staticmethod
    def info(msg: str) -> None:
        print(f"[i] {msg}")


def wiki_url(category: str | None, params: str | None, slug: str = ""):
    if slug is None:
        slug = ""

    if params is None:
        params = ""

    if category == "":
        override_url = slug
    else:
        override_url = f"Category:{category}"

    slug_req = rs.get(f"{BASE_URL}/{override_url}{params}", headers=USER_AGENT)
    return BeautifulSoup(slug_req.text, "html.parser")
