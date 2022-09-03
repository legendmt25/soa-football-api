from dependency_injector import containers, providers
from dotenv import load_dotenv
from repositories import BettingRepository
from services import BettingService

from src.integrations import UserClient, FootballClient
from src.database import Database

load_dotenv('.env.local')

class Container(containers.DeclarativeContainer): 
    config = providers.Configuration()
    config.USER_ENDPOINT.from_env("USER_ENDPOINT")
    config.FOOTBALL_ENDPOINT.from_env("FOOTBALL_ENDPOINT")
    config.DB_CONNECTION.from_env("DB_CONNECTION")
    config.PORT.from_env("PORT", as_=int, default=5000)

    wiring_config = containers.WiringConfiguration(modules=["src.endpoints"])
    db = providers.Singleton(Database, config.DB_CONNECTION)

    footballClient = providers.Factory(FootballClient, config.FOOTBALL_ENDPOINT)
    userClient = providers.Factory(UserClient, config.USER_ENDPOINT)
    bettingRepository = providers.Factory(BettingRepository, db)
    bettingService = providers.Factory(BettingService, bettingRepository, footballClient)