# Football and betting api

This app uses FastAPI with python

How to:

Start with docker-compose:
```
docker-compose up
```


Start with python locally:
```
Repeat in all services:

python -m virtualenv venv
./venv/Scripts/activate
pip install -r requirements
Add .env.local file
Update PORTS in .env.local
```

```
./soa-users-app/.env.local
KEYCLOAK_SERVER_URL=http://keycloak:8080/
KEYCLOAK_ADMIN_USERNAME=admin
KEYCLOAK_ADMIN_PASSWORD=admin

PORT=5000
```


```
./soa-football-app/.env.local
USER_ENDPOINT=http://soa-users-app:8000/
FOOTBALL_ENDPOINT=https://app.sportdataapi.com/api/v1/soccer/
FOOTBALL_API_KEY=YOUR_API_KEY

PORT=5000
```

```
USER_ENDPOINT=http://soa-users-app:8000/
FOOTBALL_ENDPOINT=http://soa-football-app:8001/
PAYMENT_ENDPOINT=http://soa-payment-app:8002/
DB_CONNECTION=postgresql://betting-app:betting-app@soa-betting-app-db:5432/betting-app

PORT=5000
```

```
USER_ENDPOINT=http://soa-users-app:8000/

DB_CONNECTION=postgresql://payment-app:payment-app@soa-payment-app-db:5432/payment-app
PORT=5000
```

