# Student Management System

## Overview
The Student Management System is a web-based application developed using Django and PostgreSQL containing the API endpoints **/students**  returns a JSON response containing a minimum of 10 with each student's name and enrolled program clearly listed.  and  **/subjects**  returns a JSON response listing all subjects associated Software Engineering program, spanning from Year 1 through 4. 

## Features
  - Endpoints to view all student 
  - Endpoints to view subject associated Software Engineering program
  

## Technologies Used
- **Backend**: Django 5.0.7, Python
- **Database**: PostgreSQL
- **Authentication**: Django's built-in authentication system
- **Deployment**: Ubuntu Server on AWS

## Installation & Setup
### Prerequisites
- Python 3.12
- PostgreSQL
- Git

### Step 1: Clone the Repository
```sh
$ git clone https://github.com/witness376/student-management.git
$ cd student-management
```

### Step 2: Create a Virtual Environment
```sh
$ python3 -m venv env
$ source env/bin/activate
```

### Step 3: Install Dependencies
```sh
$ pip install -r requirements.txt
```

### Step 4: Configure Database
Update `settings.py` with your PostgreSQL database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sma',
        'USER': 'postgres',
        'PASSWORD': '6438',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 5: Apply Migrations
```sh
$ python manage.py migrate
```

### Step 6: Create a Superuser
```sh
$ python manage.py createsuperuser
```

### Step 7: Run the Server
```sh
$ python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## Deployment on AWS
### Security Group Configuration
Allow traffic on:
- **Port 22** (SSH)
- **Port 3000** (for the Node.js frontend if applicable)

### Running the Server in Production
Use **Gunicorn** and **Nginx** for deployment.

```sh
$ gunicorn --bind 0.0.0.0:8000 student_management.wsgi
```

## Contribution
Contributions are welcome! Feel free to submit a pull request.

## License
This project is licensed under the MIT License.

---
Developed by Witness

