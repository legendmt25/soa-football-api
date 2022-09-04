from dependency_injector import containers, providers
from dotenv import load_dotenv

from src.repositories import BettingRepository
from src.services import BettingService
from src.integrations import PaymentClient, UserClient, FootballClient
from src.database import Database

load_dotenv('.env.local')

class Container(containers.DeclarativeContainer): 
    config = providers.Configuration()
    config.USER_ENDPOINT.from_env("USER_ENDPOINT")
    config.FOOTBALL_ENDPOINT.from_env("FOOTBALL_ENDPOINT")
    config.PAYMENT_ENDPOINT.from_env("PAYMENT_ENDPOINT")
    config.DB_CONNECTION.from_env("DB_CONNECTION")
    config.PORT.from_env("PORT", as_=int, default=5000)

    wiring_config = containers.WiringConfiguration(modules=["src.endpoints"])
    db = providers.Singleton(Database, config.DB_CONNECTION)

    paymentClient = providers.Factory(PaymentClient, config.PAYMENT_ENDPOINT)
    footballClient = providers.Factory(FootballClient, config.FOOTBALL_ENDPOINT)
    userClient = providers.Factory(UserClient, config.USER_ENDPOINT)
    
    bettingRepository = providers.Factory(BettingRepository, db.provided.session)
    bettingService = providers.Factory(BettingService, bettingRepository, footballClient)