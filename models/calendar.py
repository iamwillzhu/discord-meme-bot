from dataclasses import dataclass
from typing import List, Optional

from constants import HOUR
from models.meeting import Meeting, Date


@dataclass
class Calendar:
    list_of_meetings: List[Meeting]

    def create_meeting(
            self,
            created_by: str,
            start_time: int,
            start_date: Date,
            end_date: Optional[Date] = None,
            length: int = HOUR,
            recurrence: int = 1) -> None:

        new_meeting = Meeting(
            created_by=created_by,
            start_time=start_time,
            start_date=start_date,
            end_date=end_date,
            length=length,
            recurrence=recurrence,
        )

        self.list_of_meetings.append(new_meeting)

    def delete_meeting(
        self,
        position: int
    ) -> None:
        self.list_of_meetings.pop(position)

    def get_meetings_within_range(self, start_of_week: Date, end_of_week: Date):
        pass
