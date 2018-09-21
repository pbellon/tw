import argparse

from lib import config
from lib import api
from lib import utils

class App:
    description = config.DESCRIPTION
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description=self.description)
        self.api = api.init()
        self.commands = self.init_commands()
        self.run()

    def list_methods(self):
        return {
            key: utils.as_obj({
                "help": help, "action": executable
            }) for [ key, help, executable ] in self.api.list_methods()
        }

    def init_commands(self):
        methods = self.list_methods()
        for key, method in methods.items():
            self.parser.add_argument("--%s" % key, const=key,
                dest='command', action='store_const', help=method.help)
        return methods

    def run(self):
        args = self.parser.parse_args()
        if args.command:
            command = self.commands[args.command]
            print(
                command.action().as_json()
            )
        else:
            self.parser.help()

if __name__ == "__main__": App()
