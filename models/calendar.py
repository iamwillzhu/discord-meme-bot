from dataclasses import dataclass
from typing import List

from models.meeting import Meeting

@dataclass
class Calendar:
    list_of_meetings: List[Meeting]
