![gumball-api-banner](https://user-images.githubusercontent.com/94678583/215496765-7b90d67f-27cf-427b-8fdb-9abf8acb150a.png)

# The Gumball API

![](https://img.shields.io/github/license/kuroji-fusky/The-Gumball-API)

> **Note**
> Project still under construction, not production-ready yet!

The Gumball API is an open source REST and GraphQL API based from the
show *The Amazing World of Gumball* from Cartoon Network, written in Go and Python.

Project inspired by [PokéAPI](https://pokeapi.co/about) and [swapi](https://swapi.dev/about)!

## Planned endpoints
| Endpoint                | Description                                                        |
|:------------------------|:-------------------------------------------------------------------|
| `/episodes`             | Lists all the episodes from the show, including specials           |
| `/episode/:episode`     | Sends a response of an episode name, season, and other information |
| `/transcript/:episode`  | Gets a JSON response of a transcribed episode                      |
| `/season/:1..6`         | Lists all the episodes from that season                            |
| `/characters`           | Lists all the characters from the show                             |
| `/character/:name`      | Sends a response a character from a show                           |
| `/quotes/:name`         | Sends a response of all the characters' quotes                     |

### `/character{/name}`

**Request**:
```
GET /character/gumball
```

**Response** (truncated for brevity):
```json
{
  "name": "Gumball Watterson",
  "full_name": "Gumball Tristopher Watterson",
  "gender": "Male",
  "species": "Cat",
  "family": "Wattersons",
  "first_appearance": {
    "episode_title": "The DVD",
    "episode_url": "/episode/the-dvd"
  },
  "relatives": [
    {
      "name": "Darwin Watterson",
      "character_url": "/character/darwin"
    }
  ],
  "friends": [
    {
      "name": "Penny Fitzgerald",
      "character_url": "/character/penny"
    }
  ],
  "enemies": [
    {
      "name": "Rob",
      "character_url": "/character/rob"
    }
  ],
  "quotes_url": "/quotes/gumball"
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
