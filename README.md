# XCV Tenders

An application that stores government tenders.


## TASK
1. BUG: When we look at http://localhost:8000/admin/tenders/tender/ after multiple imports we see the same tenders multiple times there.
2. We want to store the reward for the tender in Bitcoin. Zloty or Euro's are not as much fun
3. We want to display the BTC reward in the admin panel.

## Installation

Create environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set up database:
```bash
python manage.py migrate
```

Create superuser:
```bash
python manage.py createsuperuser
```

Run server:
```bash 
python manage.py runserver
```
Visit (http://localhost:8000/admin/tenders/tender/)


## Importer is run daily and executes:
```bash
python manage.py import_tenders
```


## Useful links
+ [Django documentation](https://docs.djangoproject.com/en/3.1/)
+ [Polish tenders API](https://tenders.guru/pl/api)
+ [CoinCap API](https://docs.coincap.io/)



## Hints

To modify database structure run
```bash
python manage.py makemigrations
python manage.py migrate
```

To run all tests:
```bash
python manage.py test
```