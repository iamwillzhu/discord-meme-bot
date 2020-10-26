from dataclasses import dataclass
import datetime
from typing import Optional

from models.date import Date

@dataclass
class Meeting:
    start_date: Date
    end_date: Optional[Date]
    start_time: int
    length: int
    created_by: str
    recurrence: int = 1

