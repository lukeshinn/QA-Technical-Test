# GET
**Description:** Look up schedule of a certain team
| Request Method |      Endpoint |  Format |
|----------|-------------|------------------------------------------|
| GET |  {base.url}/teams/{sqlId}/schedule/{gameId}/entry/{opponentId} | JSON |

| Paramater   |      Data Type      | Description |
|----------|:-------------:|--------------|
| sqlId |  integer | unique identifier for each coach |
| gameId |  integer | identifier for game/sport  |
| opponentId |  integer | unique identifier for each opponent|
#### Example Response
Here is an example of expected results for each error code
**Response code:** 200
```javascript
{
  "opponentId":123456,
  "opponent":TestOpponent,
  "isHome":true,
  "gameType":0,
  "categories": [{
    "homeTeamScore":4,
    "awayTeamScore":"5",
  }],
}
```
**Response code:** 401 - user is not logged in
**Response code:** 403 - user was authenticaed but issue with certificate is present
**Response code:** 404 - user is logged in but one or more paramaters are invalid
**Response code:** 500 - browser could contain cached credentials

# PUT
**Description:** Update a single schedule of an event
| Request Method |      Endpoint |  Format |
|----------|-------------|------------------------------------------|
| PUT |  {base.url}/teams/{sqlId}/schedule/{gameId}/entry/{opponentId} | JSON |

| Paramater   |      Data Type      | Description |
|----------|:-------------:|--------------|
| sqlId |  integer | unique identifier for each coach |
| gameId |  integer | identifier for game/sport  |
| opponentId |  integer | unique identifier for each opponent|
#### Example Response
**Response code:** 200
```javascript
{
  "gameId":1234567,
  "opponentId":123456,
  "opponent":TestOpponent,
  "isHome":true,
  "gameType":0,
  "categories": [{
    "homeTeamScore":4,
    "awayTeamScore":"5",
  }],
  "updated_at":"2019-11-20T14:33:58Z"
}
```
**Response code:** 404 - user is logged in but one or more paramaters are invalid

# POST
**Description:** Create a new event
| Request Method |      Endpoint |  Format |
|----------|-------------|------------------------------------------|
| POST |  {base.url}/teams/{sqlId}/schedule/{gameId}/entry/create | JSON |

| Paramater   |      Data Type      | Description |
|----------|:-------------:|--------------|
| sqlId |  integer | unique identifier for each coach |
| gameId |  integer | identifier for game/sport  |
| opponentId |  integer | unique identifier for each opponent|
#### Example Response
**Response code:** 200
```javascript
{
  "gameId":1234567,
  "opponentId":123456,
  "opponent":TestOpponent,
  "isHome":true,
  "gameType":0,
  "matchScore": [{
    "homeTeam":4,
    "awayTeam":"5",
  }],
  "created_at":"2019-11-20T14:33:58Z"
  "updated_at":"2019-11-20T14:33:58Z"
}
```
**Response code:** 401 - game is in progress and is unavailable to be updated
**Response code:** 404 - game has been removed

# DELETE
**Description:** Create a new event
| Request Method |      Endpoint |  Format |
|----------|-------------|------------------------------------------|
| DELETE |  {base.url}/teams/{sqlId}/schedule/{gameId}/entry/{opponentId} | JSON |

| Paramater   |      Data Type      | Description |
|----------|:-------------:|--------------|
| sqlId |  integer | unique identifier for each coach |
| gameId |  integer | identifier for game/sport  |
#### Example Response
**Response code:** 200
```javascript
{  }
```
**Response code:** 401 - user does not have delete permission on this entry
