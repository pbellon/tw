import argparse
import utils
import api

class App:
    description = utils.config.DESCRIPTION
    def __init__(self):
        self.init_parser()
        self.init_api()
        self.init_commands()
        self.run()

    def init_parser(self): self.parser = argparse.ArgumentParser(description=self.description)

    def init_api(self): self.api = api.init()

    def init_commands(self):
        self.commands = {}

        for method in self.api.list_methods():
            [ key, help, executable ] = method
            self.commands[key] = {
                "help": help,
                "action": executable
            }

        for key, command in self.commands.items():
            self.parser.add_argument(
                "--%s" % key,
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
        print(result.as_json())

if __name__ == "__main__": App()
