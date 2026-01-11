python -m venv venv
Automatically (From Existing venv)
pip freeze > requirements.txt
pip install -r .\requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py migrate converse
python manage.py makemigrations converse
python manage.py dbupgrade
python manage.py dbupgrade entity-types-v-1

For running botstudio
.\venv\Scripts\activate  Then enter

For create super user ====>
python manage.py createsuperuser
http://127.0.0.1:8000/
(create org, license, customer, user)

for run the application
python .\manage.py runserver