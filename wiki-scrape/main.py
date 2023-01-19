from utils import wiki_url
import re
import json


def main():
    temp_list: list[dict[str, str]] = []
    alphabet_list = [chr(x).upper() for x in range(97, 123)]

    # TODO filter these via regex
    REGEX_FILTER = ["/Enemies",
                    "/People",
                    "Character",
                    "Category:",
                    "Thread:",
                    "parents",
                    "family",
                    "shareholders",
                    "babies",
                    "guards",
                    "clones"]

    for letter in alphabet_list:
        character = wiki_url(category="Characters", params=f"?from={letter}")
        character_item = character.select("a.category-page__member-link")

        for char in character_item:
            temp_list.append({
                'name': char['title'],
                'url': char['href']
            })

        print(f"appended items from '{letter}'")

        # orig 290

    with open("test.json", "a+", encoding="utf-8") as f:
        json.dump({"characters": temp_list}, f, indent=4)


if __name__ == "__main__":
    main()
