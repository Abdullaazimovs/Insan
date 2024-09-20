# Insan project

## Installation virtual environment

1. Download Python 3.10

2. Set up venv
```bash
   python3 -m venv name
```

3. Activation
```bash
   .\env\Scripts\activate - for Windows
   source env/bin/activate - Linux/MacOS 
```

4. Install the required libraries using the command:
```bash
python -m pip install -r requirements.txt
```

## Setings 
For setting up DB go to the ./.envs/.postgres/ create file .postgres

Here u can find more about postgres: "https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e"


### Launching API 

### Docker
To run the bot, it is recommended to use Docker.

More details: https://docs.docker.com/

To start the project, enter the following command in the terminal:
```bash
docker-compose up
```
To run the project in the background, you need to enter the following command in the terminal:
```bash
docker-compose up -d
```

### Terminal 
To run the bot natively through the Python interpreter, you need to enter the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Before running natively through the terminal, you need to ensure that the Postgres database is running on your local machine and that the necessary database configurations are in place.

### Urls 

/api/register/ - for registration a user 

/api/login/ - for login a user

/api/logout/ - for logout a user

/api/category_list/ - to create and see the category 

/api/portfolio_list/ - to create and see the portfolio

/api/portfolio_detail/<int:pk>/ - to edit or delete portfolio

/api/portfolio/<int:portfolio_id>/blocks/ - to see all the blocks whitch created for portfolio or create block

/api/portfolio_detail/<int:portfolio_id>/block/<int:block_id>/ - to update or delete block



