from typing import Iterable, Optional

from src.integrations import FootballClient
from src.enums import OddsType
import src.models as models

class FootballService:
    def __init__(self, footballClient: FootballClient, leagues_id: str):
        self.footballClient = footballClient
        self.leagues_id = [int(league_id) for league_id in leagues_id.split(',')]

    def findAllMatches(self, seasonId: Optional[int], live: Optional[int]) -> Iterable[models.Match]:
        if(seasonId != None and live != None):
            return self.footballClient.findAllLiveMatchesBySeasonId(seasonId)
        if(seasonId != None):
            return self.footballClient.findAllMatches(seasonId)
        if(live != None):
            return self.footballClient.findAllLiveMatches()
        return []

    def findMatchById(self, id: int, seasonId: int) -> models.Match:
        return self.footballClient.findMatchById(id, seasonId)

    def findAllLeagues(self, countryId: Optional[int] = None) -> Iterable[models.League]:
        if(countryId == None):
            return self.footballClient.findAllLeagues()
        return self.footballClient.findAllLeaguesByCountry(countryId)

    def findLeagueById(self, id: int) -> models.League:
        return self.footballClient.findLeagueById(id)

    def findAllSeasons(self, leagueId: int) -> Iterable[models.Season]:
        return self.footballClient.findAllSeasons(leagueId)

    def findSeasonById(self, id: int, leagueId: int) -> models.Season:
        return self.footballClient.findSeasonById(id, leagueId)

    def findOddsByMatchId(self, matchId: int, type: OddsType):
        return self.footballClient.findOddsByMatch(matchId, type)

