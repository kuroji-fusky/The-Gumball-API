BASE_URL: str = "https://theamazingworldofgumball.fandom.com/wiki/"

USER_AGENT: dict[str, str] = {
	"User-Agent": (
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
		"AppleWebKit/537.36 (KHTML, like Gecko)"
		"Chrome/45.0.2454.101 Safari/537.36"
	),
	"referer": BASE_URL
}


class Status:
	@staticmethod
	def error(msg: str) -> None:
		print(f"[ERROR] {msg}")
	
	@staticmethod
	def info(msg: str) -> None:
		print(f"[i] {msg}")