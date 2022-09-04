from enum import Enum


class MatchStatus(Enum):
    NOT_STARTED = 0
    IN_PLAY = 1
    UPDATE_LATER = 2
    ENDEN = 3
    POSTPONED = 4
    CANCELLED = 5
    ABANDONED = 6
    INTERRUPTED = 7
    SUSPENDED = 8
    AWARDED = 9
    DELAYED = 10
    HALF_TIME = 11
    EXTRA_TIME = 12
    PENALTIES = 13
    BREAK_TIME = 14
    AWARDING = 15
    TO_BE_ANNOUNCE = 17
    AFTER_PENALTIES = 31
    AFTER_EXTRA_TIME = 32

class OddsType(Enum):
    PREMATCH = 'prematch'
    INPLAY = 'inplay'