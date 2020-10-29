from dataclasses import dataclass


from models.calendar import Calendar
from models.date import Date
from view import View


@dataclass
class Controller:
    model: Calendar
    view: View

    def create_meeting(self)

    def show_day_meetings(self, current_day: Date):
        meetings = self.model.get_meetings_within_range(
            start_of_week=current_day,
            end_of_week=current_day
        )

        return self.view.show_meetings(meetings=meetings)
