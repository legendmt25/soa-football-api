from dependency_injector import containers, providers
from dotenv import load_dotenv

from src.services import UserService

load_dotenv('.env.local')

class Container(containers.DeclarativeContainer): 
    config = providers.Configuration()
    config.KEYCLOAK_SERVER_URL.from_env("KEYCLOAK_SERVER_URL")
    config.KEYCLOAK_ADMIN_USERNAME.from_env("KEYCLOAK_ADMIN_USERNAME")
    config.KEYCLOAK_ADMIN_PASSWORD.from_env("KEYCLOAK_ADMIN_PASSWORD")
    config.PORT.from_env("PORT", as_=int, default=5000)

    wiring_config = containers.WiringConfiguration(modules=["src.endpoints"])
    userService = providers.Factory(UserService, config.KEYCLOAK_SERVER_URL, config.KEYCLOAK_ADMIN_USERNAME, config.KEYCLOAK_ADMIN_PASSWORD)