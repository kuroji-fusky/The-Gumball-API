from utils import wiki_url
import re
from concurrent.futures import ThreadPoolExecutor


def main():
	temp_list: list[dict[str, str]] = []
	alphabet_list = [chr(x).upper() for x in range(97, 123)]
	
	for letter in alphabet_list:
		character = wiki_url(category="Characters", params=f"?from={letter}")
		character_item = character.select("a.category-page__member-link")
		
		for char in character_item:
			temp_list.append({
				'name': char['title'],
				'url': char['href']
			})
		
		print(f"added items from '{letter}'")
	
	filter_list = ["/Enemies", "/People", "Character", "Category:", "Thread:",
				   "parents", "family", "shareholders", "babies", "guards", "clones", "lookalike"]
	regex_filter = rf"({')|('.join(filter_list)})"
	
	for char in temp_list:
		name = char["name"]
		matches = re.findall(regex_filter, name, re.IGNORECASE)
		
		if not matches:
			print(f"[YES] {name}")
		else:
			print(f"[---] {name}")


if __name__ == "__main__":
	with ThreadPoolExecutor(max_workers=200) as e:
		e.map(main(), range(250))  # NOQA
