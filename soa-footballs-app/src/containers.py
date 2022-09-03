from dependency_injector import containers, providers
from dotenv import load_dotenv

from src.integrations import UserClient, FootballClient
from src.services import FootballService

load_dotenv('.env.local')

class Container(containers.DeclarativeContainer): 
    config = providers.Configuration()
    config.USER_ENDPOINT.from_env("USER_ENDPOINT")
    config.FOOTBALL_ENDPOINT.from_env("FOOTBALL_ENDPOINT")
    config.PORT.from_env("PORT", as_=int, default=5000)
    config.FOOTBALL_API_KEY.from_env("FOOTBALL_API_KEY")

    wiring_config = containers.WiringConfiguration(modules=["src.endpoints"])    

    userClient = providers.Factory(UserClient, config.USER_ENDPOINT)
    footballClient = providers.Factory(FootballClient, config.FOOTBALL_ENDPOINT, config.FOOTBALL_API_KEY)
    footballService = providers.Factory(FootballService, footballClient)