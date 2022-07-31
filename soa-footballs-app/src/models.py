from datetime import date
from typing import Optional

from src.enums import MatchStatus

class Team:
    team_id: int
    name: str
    short_code: str

class Stats:
    home_score: int
    away_score: int
    ht_score: Optional[str]
    ft_score: Optional[str]
    et_score: Optional[str]
    ps_score: Optional[str]
    

class Match:
    match_id: int
    status_code: MatchStatus
    status: str
    match_start: date
    league_id: int
    season_id: int
    home_team: Team
    away_team: Team
    stats: Stats

class League:
    league_id: int
    country_id: int
    name: str

class Season:
    season_id: int
    name: str
    is_current: int
    country_id: int
    league_id: int
    start_date: date
    end_date: date

class Venue:
    venue_id: int
    country_id: int
    capacity: int
    city: str
    name: str

class Country:
    country_id: int
    name: str
    country_code: str
    continent: str