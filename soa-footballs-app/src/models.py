from datetime import date
from typing import Optional
from pydantic import BaseModel

class Fixture:
    id: int
    timezone: str
    date: date
    timestamp: int
    status: any
    

class Result:
    home: Optional[int]
    away: Optional[int]

class Score:
    halftime: Result
    fulltime: Result
    extratime: Result
    penaly: Result

class Team:
    id: int
    name: str

class Teams:
    home: Team
    away: Team

class League:
    id: int
    name: str
    country: str
    season: int
    
class FixtureBase(BaseModel):
    pass

class Fixtures(FixtureBase):
    id: int
    fixture: Fixture
    score: Score
    league: League
    teams: Teams
    


