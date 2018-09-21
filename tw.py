import argparse

from lib import config
from lib import api

class App:
    description = config.DESCRIPTION
    def __init__(self):
        self.init_argparser()
        self.init_api()
        self.init_commands()
        self.run()

    def init_argparser(self):
        self.parser = argparse.ArgumentParser(
            description=self.description)

    def init_api(self):
        self.api = api.init()

    def list_api_methods(self):
        return self.api.list_methods()

    def init_commands(self):
        self.commands = {
            key: {
                "help": help, "action": executable
            } for [ key, help, executable ] in self.list_api_methods()
        }

        for key, command in self.commands.items():
            self.parser.add_argument(
                "--%s" % key,
                action='store_const',
                dest='command',
                const=key,
                help=command["help"])

    def run(self):
        parser = self.parser
        args = parser.parse_args()
        self.call(args.command) if args.command else parser.print_help()

    def call(self, command_key):
        command = self.commands[command_key]
        result = command['action']()
        print(result.as_json())

if __name__ == "__main__": App()
