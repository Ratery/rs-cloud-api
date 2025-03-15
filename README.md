An API for the **[Menu-App](https://github.com/verevka8/menu_app_general)** (see for more info) project to manage users, restaurants and dishes.

## Launch instructions

1. Create and set up the `.env` file:
```env
DB_HOST = postgres
DB_PORT = 5432
DB_NAME = fast_api
DB_USER = <USER>
DB_PASSWORD = <PASSWORD>
SECRET_KEY = <SECRET_KEY>
ALGORITHM = HS256
```

2. Run `docker-compose`:
```bash
docker-compose up -d
```

Application will be available at `localhost:8000`.

### Adding sample data

To add sample data (restaurants and dishes) to the database run:
```bash
docker-compose exec app python -m app.init_db
```

## Documentation

After launching the application, the documentation will be available at `localhost:8000/docs`.

Also, you can see the [documentation](https://verevka8.github.io/menu_app_general/ApiDocumentation.html) in the **Menu-App** repository.
