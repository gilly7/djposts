"# djposts" 

### how to get started

Ensure you are running the latest version of python.
- clone the project
- create virtual environment
```
python3 -m pip install virtualenv
python3 -m venv <env-folder>
```
- activate the virtual environment

```
source /<path to venv>/bin/activate
```
install django
```
pip install django
```

### Running the Project
Make migrations
```
python manage.py makemigrations
```
Apply the migrations
```
python manage.py migrate
```

Run the server
```
python manage.py runserver
```

Inspired by: [citzix blog](https://citizix.com/getting-started-with-django-a-simple-crud-application/)




