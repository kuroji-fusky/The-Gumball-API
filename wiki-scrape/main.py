from concurrent.futures import ThreadPoolExecutor
from utils import wiki_url
import re
import json


def main():
	temp_list: list[dict[str, str]] = []
	alphabet_list = [chr(x).upper() for x in range(97, 123)]
	
	try:
		print("cache.json found, appending data...")
		
		with open("cache.json", 'r') as fuck:
			temp_list = json.load(fuck)["characters"]
	
	except FileNotFoundError:
		print("cache.json not found, will generate anyway")
		
		for letter in alphabet_list:
			character = wiki_url(category="Characters", params=f"?from={letter}")
			character_item = character.select("a.category-page__member-link")
			
			for char in character_item:
				temp_list.append({
					'name': char['title'],
					'url': char['href']
				})
			
			print(f"added items from letter {letter}")
		
		with open("cache.json", "a+") as f:
			json.dump({'characters': temp_list}, f, indent=4, ensure_ascii=True)
	
	prefixes = ["/Enemies", "/People", "Character", "Category:", "Thread:"]
	categories = ["parents", "family", "shareholders", "babies", "guards", "clones", "lookalike"]
	
	regex_filter = rf"({')|('.join([*prefixes, *categories])})"
	
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
