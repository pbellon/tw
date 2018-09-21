
import ipdb
import twitter
import json
import env
import argparse

class TwitterApi:
    def __init__(self):
        self.api = twitter.Api(
            consumer_secret=env.CONSUMER_SECRET,
            consumer_key=env.CONSUMER_KEY,
            access_token_key=env.ACCESS_TOKEN_KEY,
            access_token_secret=env.ACCESS_TOKEN_SECRET
        )

    def retweets(self):
        return self.api.GetUserRetweets()

    def timeline(self):
        return self.api.GetUserTimeline()

class App:
    description = 'Small utility to get user data (tweets and retweets)'

    def __init__(self):
        self.init_parser()
        self.init_api()
        self.init_commands()
        self.run()

    def init_parser(self): self.parser = argparse.ArgumentParser(description=self.description)

    def init_api(self): self.api = TwitterApi()

    def init_commands(self):
        self.commands = {
            "--retweets": {
                "action": self.api.retweets,
                "help": 'Get user latest retweets',
            },
            "--timeline": {
                "action": self.api.timeline,
                "help": 'Get user timeline (limited)'
            }
        }

        for key, command in self.commands.items():
            self.parser.add_argument(key,
                action='store_const',
                dest='command',
                const=key,
                help=command["help"]
            )

    def run(self):
        args = self.parser.parse_args()
        if args.command:
            self.call_command_action(args.command)
        else:
            self.parser.print_help()

    def call_command_action(self, command_key):
        command = self.commands[command_key]
        result = command['action']()
        json_result = self.as_json(result)
        print(json_result)

    def as_json(self, tweets):
        return json.dumps(
            list(map(lambda tweet: json.loads(tweet.AsJsonString()), tweets)),
            indent=4
        )


if __name__ == "__main__": App()
