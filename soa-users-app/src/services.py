from keycloak import KeycloakOpenID, KeycloakAdmin

from src.models import User

class UserService:
    def __init__(self, serverUrl: str, adminUsername: str, adminPassword: str, realm: str = 'master') -> None:
        self.keycloakAdmin = KeycloakAdmin(
            server_url=serverUrl,
            realm_name=realm,
            username=adminUsername,
            password=adminPassword
        )

        client = 'soa-users-app'
        self.keycloakAdmin.create_client(payload={ 'clientId': client }, skip_exists=True)        
        self.keycloak = KeycloakOpenID(
            server_url=serverUrl,
            client_id=client,
            client_secret_key='UHQ5OpeETwkU81tkv6i8ko9pHQHQLldE',
            realm_name=realm,
        )
    
    def register(self, data: User):
        return self.keycloakAdmin.create_user(payload={
            'username': data.username,
            'email': data.email,
            'credentials': [{ 'type': 'password', 'value': data.password }],
            'firstName': data.firstName,
            'lastName': data.lastName
        })

    def userInfo(self, token: str):
        return self.keycloak.userinfo(token=token)
