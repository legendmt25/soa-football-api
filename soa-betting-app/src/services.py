from repositories import BettingRepository
from src.integrations import FootballClient
import src.models as models

class BettingService:
    def __init__(self, bettingRepository: BettingRepository, footballClient: FootballClient):
        self.footballClient = footballClient
        self.bettingRepository = bettingRepository

    def placeBet(matchId: int, bet: str):
        pass

