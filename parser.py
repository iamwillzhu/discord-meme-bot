from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Parser:
    command: str
    receiver: Optional[str] = None
    amount: Optional[int] = None

    @classmethod
    def parse_message(cls, message: str):
        arguments = message.split(" ")
        command = arguments[1]
        receiver = arguments[2]
        amount = int(arguments[3])

        return cls(
            command=command,
            receiver=receiver,
            amount=amount)
