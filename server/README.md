## Available Scripts for Django
The following commands are for the user on this app.

Install django on your PC
### `pip3 install django`

Working with database:
### `python manage.py makemigrations`

Than migrate: 
### `python manage.py migrate`

Create superuser:
### `python manage.py createsuperuser`

In the project directory, you can run:

### `python manage.py runserver`

Runs the app in the development mode.<br>
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

The page will reload if you make edits.<br>
You will also see any lint errors in the console.

### `python manage.py test blockchain`

Launches the test runner in the interactive watch mode.<br>
See the section about [running tests](https://gitlab.com/crypto-thesis/thesis/tree/master/django_project/blockchain/tests) for more information.<br>

The following commands are for Postgres DB running on this app.
### `sudo su - postgres`

To enter the postgres shell write:
### `psql`
