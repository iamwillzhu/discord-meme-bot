from dataclasses import dataclass


@dataclass(frozen=True)
class Date:
    day: int
    month: int
    year: int

    def __eq__(self, other):
        return (self.year, self. month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __le__(self, other):
        return (self.year, self.month, self.day) <= (other.year, other.month, other.day)

    def __ge__(self, other):
        return (self.year, self.month, self.day) >= (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def __str__(self):
        return "{:02d}/{:02d}/{:04d}".format(
            self.month, self.day, self.year
        )
