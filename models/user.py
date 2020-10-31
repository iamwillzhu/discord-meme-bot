from dataclasses import dataclass
from typing import DefaultDict


@dataclass
class User:
    name: str
    expenses: DefaultDict[str, int]
