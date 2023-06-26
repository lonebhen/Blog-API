# API Blog Post with Django REST Framework (DRF)

This repository contains the code and resources for an API blog post created using Django REST Framework (DRF). 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

To get started with this project, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/lonebhen/Blog-API


cd blog-api

Set up a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

Run database migrations:

python manage.py makemigrations
python manage.py migrate

Usage
Once the installation is complete, you can start the development server using the following command:

python manage.py runserver
Access the API at http://localhost:8000/. You can now interact with the API using your preferred tool, such as cURL, Insomia or Postman.



API Endpoints
The API provides the following endpoints:

/auth/signup/: (POST) - Signup user
/auth/login/: (POST) - Login user




/blog/posts/: (GET, POST) - Get all posts or create a new post.
/blog/posts/{id}/: (GET, PUT, PATCH, DELETE) - Retrieve, update, or delete a specific post.
/blog/public/: (GETT) - Get all posts for the public



