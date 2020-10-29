from dataclasses import dataclass
import datetime
from typing import Optional

from models.date import Date


@dataclass
class Meeting:
    start_time: int
    created_by: str
    start_date: Date
    end_date: Optional[Date]
    start_time: int
    length: int
    recurrence: int

    # TODO: I probably don't even need this because we I want to be able to have the view class structure into a column view
    def __str__(self):
        return f"Start Date: {self.start_date}, Created By: {self.created_by}, Start Time: {self.start_time}, Length: {self.length}"
