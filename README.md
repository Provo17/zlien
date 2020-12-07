# zlien

System Requirements:
- Python 3 https://www.python.org/
- PIP https://pip.pypa.io/en/stable/
- Virtual Environment https://docs.python.org/3/library/venv.html
- Django - https://www.djangoproject.com/

Installation and Usage:
- Ensure that python and PIP is installed

- Using the terminal navigate to the project directory and PIP install Virtual Environment

- Start Virtual environment with the command
```source {env_name}/bin/activate```

- Navigate to django project root (The root is on the smae directory level as the manage.py and requirements.txt files)

- Install dependecies
```pip install -r requirements.txt```

- To run the application type the following command in the terminal and navigate to http://localhost:8000/ in the browser
```python manage.py runserver```


Mock Data can be downloaded usinf this link and clicking the green Download Data button: https://www.mockaroo.com/180bf580

10% of the data is missing a required field and 5% of the data has no commencement date.

After data upload Users can view and edit data by navigating to the link below and using the provided credentials

Admin Login:
http://localhost:8000/admin/
username: admin
password: zlien2020
