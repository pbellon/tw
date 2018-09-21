import argparse

from lib import config
from lib import api
from lib import utils

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
            key: utils.as_obj({
                "help": help, "action": executable
            }) for [ key, help, executable ] in self.list_api_methods()
        }

        for key, command in self.commands.items():
            self.parser.add_argument("--%s" % key, const=key,
                dest='command', action='store_const', help=command.help)

    def parse_args(self): return self.parser.parse_args()
    def help(self): self.parser.print_help()

    def run(self):
        args = self.parse_args()
        if args.command:
            command = self.commands[args.command]
            print(
                command.action().as_json()
            )
        else:
            self.help()

if __name__ == "__main__": App()
