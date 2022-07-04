# **Doctors**

#### About
This is a pet-project, it should not be used for commercial purposes!
<br/>REST API with an administrative panel that allows you to add, edit, 
<br/>delete, filter and search entities (Directions, Doctors), 
<br/>returns a list of all entities with the possibility of filtering.

##### Software that you need
* Python 3.8.
* Django 3.2.
* MySQL.

##### Technology stack:
* Python 3.8, Django 3.2;
* MySQL;
* Django REST framework.

##### Getting Started
* Create database 'doctors' in MySQL.
* Update database settings in settings.py, if necessary.
* `$ pip install -r requirements.txt`
* `$ python manage.py makemigrations`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

##### Testing application for administrators
* `$ python manage.py createsuperuser`
* Enter your desired username, email, password.
* `Username: admin`
* `Email address: admin@example.com`
* `Password: password12Q`
* `Password (again): password12Q`
* `Superuser created successfully.`

##### API endpoints
* `api/medic/Direct/` - Returns a list of all destinations.
* `api/medic/Doctor/` - Returns a list of all doctors.
* `api/medic/Direct/id` - Returns data about the direct
* `api/medic/Doctor/id` - Returns data about the doctor


Made by `Self`.