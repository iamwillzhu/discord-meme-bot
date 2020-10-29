from dataclasses import dataclass


@dataclass
class Parser:
    command: str

    @classmethod
    def parse_message(cls, message: str):
        arguments = message.split(" ")
        command = arguments[1]
        return cls(command)
