# The Gumball API

> **Note**
> Project still under construction, not production-ready yet!

The Gumball API is an open source REST and GraphQL API based from the
show "The Amazing World of Gumball" from Cartoon Network.

Inspired by [PokéAPI](https://pokeapi.co/about) and [swapi](https://swapi.dev/about)!

## Planned endpoints
| Endpoint                | Description                                                        |
|:------------------------|:-------------------------------------------------------------------|
| `/episodes`             | Lists all the episodes from the show, including specials           |
| `/episode{/episode}`    | Sends a response of an episode name, season, and other information |
| `/transcript{/episode}` | Gets a JSON response of a transcribed episode                      |
| `/season{/1..6}`        | Lists all the episodes from that season                            |
| `/characters`           | Lists all the characters from the show                             |
| `/character{/name}`     | Sends a response a character from a show                           |
| `/quotes{/name}`        | Sends a response of all the characters' quotes                     |
| `/families`             | Lists all the families from the show                               |

### `/character{/name}`

Request:
```
https://tawog-api.kurofusky.xyz/character/gumball
```

Response (truncated for brevity):
```json
{
  "name": "Gumball Watterson",
  "full_name": "Gumball Tristopher Watterson",
  "gender": "Male",
  "species": "Cat",
  "family": "Wattersons",
  "relatives": [
    "https://tawog-api.kurofusky.api/character/darwin",
    "https://tawog-api.kurofusky.api/character/anais",
    "https://tawog-api.kurofusky.api/character/nicole",
    "..."
  ],
  "friends": [
    "https://tawog-api.kurofusky.api/character/darwin",
    "https://tawog-api.kurofusky.api/character/penny",
    "https://tawog-api.kurofusky.api/character/carrie",
    "..."
  ],
  "enemies": [
    "https://tawog-api.kurofusky.api/character/rob",
    "https://tawog-api.kurofusky.api/character/miss_simian",
    "https://tawog-api.kurofusky.api/character/jamie",
    "..."
  ],
  "first_appearance": "https://tawog-api.kurofusky.xyz/episode/the-dvd",
  "quotes": "https://tawog-api.kurofusky.xyz/quotes/gumball"
}
```


## Technology stack

[![Tech Stack](https://skillicons.dev/icons?i=py,fastapi,graphql,cloudflare)](https://skillicons.dev)

The Gumball API is built with FastAPI, all responses are formatted in JSON.

## Legal stuff

*The Amazing World of Gumball* and all its assets are trademarks of
Turner Broadcasting System, Inc.

All data is sourced from [*The Amazing World of Gumball Wiki*][wiki] and the
project's source code is completely open source under the MIT license.

[wiki]: https://theamazingworldofgumball.fandom.com