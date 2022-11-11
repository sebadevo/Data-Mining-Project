from enum import Enum

class Type(Enum):
    Tram = 0
    Metro = 1
    Bus = 3


class Day(Enum):
    Weekday = "weekday"
    Saterday = "saturday"
    Sunday = "sunday"