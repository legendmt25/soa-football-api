from dependency_injector import containers, providers
from dotenv import load_dotenv

from src.database import Database
from src.integrations import UserClient
from src.repositories import TransactionRepository
from src.services import TransactionService

load_dotenv('.env.local')

class Container(containers.DeclarativeContainer): 
    config = providers.Configuration()
    config.DB_CONNECTION.from_env("DB_CONNECTION")
    config.USER_ENDPOINT.from_env("USER_ENDPOINT")
    config.PORT.from_env("PORT", as_=int, default=5000)

    wiring_config = containers.WiringConfiguration(modules=["src.endpoints"])    
    db = providers.Singleton(Database, config.DB_CONNECTION)


    transactionRepository = providers.Factory(TransactionRepository, db.provided.session)
    transactionService = providers.Factory(TransactionService, transactionRepository)
    userClient = providers.Factory(UserClient, config.USER_ENDPOINT)