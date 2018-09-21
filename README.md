# getTweets.py
```
usage: getTweets.py [-h] [--retweets] [--timeline]

Small utility to get user data (tweets and retweets)

optional arguments:
  -h, --help  show this help message and exit
  --retweets  Get user latest retweets
  --timeline  Get user timeline (limited)
```

## Installation
```sh
pip install -r requirement.txt
```

## Configuration
```sh
mv env.sample.py env.py
```
Then edit env.py to add the proper key & secrets. To obtain them visit [twitter apps][apps] and create an app if necessary.

[apps]: https://apps.twitter.com/
