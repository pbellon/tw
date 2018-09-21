import twitter
import json
from . import env

class TwitterApiResult:
    def __init__(self, tweets):
        self.tweets = tweets

    def as_list(self): return self.tweets

    def as_json(self): return json.dumps(
            list(
                map(
                    lambda tweet: json.loads(tweet.AsJsonString()),
                    self.tweets
                )
            ),
            indent=4
        )

def api_result(tweets): return TwitterApiResult(tweets=tweets)

class TwitterProxy:
    def __init__(self):
        self.api = twitter.Api(
            consumer_secret=env.CONSUMER_SECRET,
            consumer_key=env.CONSUMER_KEY,
            access_token_key=env.ACCESS_TOKEN_KEY,
            access_token_secret=env.ACCESS_TOKEN_SECRET
        )
        self.register_method('GetUserRetweets')
        self.register_method('GetUserTimeline')

    def register_method(self, method_name):
        def __proxy(self, method_name):
            return lambda: api_result(
                getattr(
                    self.api,
                    method_name
                )()
            )

        setattr(self, method_name, __proxy(self, method_name))

class TwitterApi:
    __methods = (
        ("retweets", "Get user latest retweets"),
        ("timeline", "Get user latest timeline"),
    )

    def __init__(self):
        self.latest_result = None
        self.api = TwitterProxy()

    def list_methods(self):
        return list(
            map(
                lambda m: m + (getattr(self, m[0]),),
                self.__methods
            )
        )

    def retweets(self):
        return self.api.GetUserRetweets()

    def timeline(self):
        return self.api.GetUserTimeline()


def init(): return TwitterApi()
