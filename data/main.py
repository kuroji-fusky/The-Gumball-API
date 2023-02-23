import json
import re
from concurrent.futures import ThreadPoolExecutor
from utils import wiki_url


def main():
    temp_list: list[dict[str, str]] = []
    characters_list: list[dict[str, str]] = []
    alphabet_list: list[str] = [chr(x).upper() for x in range(97, 118)]

    try:
        with open("cache.json", 'r', encoding='utf-8') as f:
            temp_list = json.load(f)["characters"]

        print("cache.json found, appending data...")

    except FileNotFoundError:
        print("cache.json not found, will generate anyway")

        for letter in alphabet_list:
            character = wiki_url(category="Characters",
                                 params=f"?from={letter}")
            character_item = character.select("a.category-page__member-link")

            for char in character_item:
                temp_list.append({'name': char['title'], 'url': char['href']})

            print(f"added items from letter {letter}")

        with open("cache.json", "a+", encoding='utf-8') as f:
            json.dump({'characters': temp_list},
                      f,
                      indent=4,
                      ensure_ascii=True)

    url_modifiers = [
        "/Enemies", "/People", "/Objects", "Character", "Category:", "Thread:"
    ]

    categories = [
        "parents", "family", "shareholders", "babies", "guards", "clones",
        "lookalike"
    ]

    regex_filter = rf"({')|('.join([*url_modifiers, *categories])})"

    for char in temp_list:
        name = char["name"]
        url = char["url"]
        matches = re.findall(regex_filter, name, re.IGNORECASE)

        if not matches:
            characters_list.append({'name': name, 'url': url})

    print(characters_list)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=200) as e:
        e.map(main(), range(250))  # NOQA
