# Django User Signup and Signin Flow

This project implements a basic user signup and signin flow using Django, a high-level Python web framework.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Running Tests](#running-tests)
- [Run Command](#run-command)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration with email and password
- User login with email and password
- Password hashing for security
- Basic user authentication and session management

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Virtualenv (optional but recommended)

### Steps

1. *Clone the repository:*

```bash
git clone https://github.com/krishppuria/demoUri_api
cd django-user-signup-signin
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
