from dependency_injector import containers, providers
from dotenv import load_dotenv
from services import FootballService

from src.integrations import UserClient, FootballClient

load_dotenv('.env.local')

class Container(containers.DeclarativeContainer): 
    config = providers.Configuration()
    config.USER_ENDPOINT.from_env("USER_ENDPOINT")
    config.FOOTBALL_ENDPOINT.from_env("FOOTBALL_ENDPOINT")
    config.PORT.from_env("PORT", as_=int, default=5000)

    wiring_config = containers.WiringConfiguration(modules=["src.endpoints"])    

    userClient = providers.Factory(UserClient, config.USER_ENDPOINT)
    footballClient = providers.Factory(FootballClient, config.USER_ENDPOINT)
    footballService = providers.Factory(FootballService, footballClient)