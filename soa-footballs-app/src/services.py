from datetime import date
from io import BytesIO
from typing import Iterable
from integrations import FootballClient

import src.models as models

class FootballService:
    def __init__(self, footballClient: FootballClient):
        self.footballClient = footballClient

    def findAllFixtures(self):
        return self.footballClient.findAllFixtures()