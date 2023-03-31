"""ReqexParser - parser"""
import re


class RegexParser:
    """ReqexParser - parser main class"""

    def __init__(self):
        self.exp = ""
        self.string = ""

    def parse_string(self):
        """Parse and print result"""
        print((re.match(self.exp, self.string) is not None))

    def main_loop(self):
        """Main loop"""
        while True:
            command = input(">")
            self.exp, self.string = command.split(sep="|")
            self.parse_string()
