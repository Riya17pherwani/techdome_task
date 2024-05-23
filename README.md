# Django Todo Application

## Overview

This project is a Django-based web application with two main API sections: `TodoController` and `AuthController`. The application uses a SQL Server database and implements role-based access control to manage authorization.

## Features

### TodoController
- **CRUD APIs for Todo Items**
  - `GET /get/{id}`: Get a single todo item.
  - `GET /getall`: Get all todo items.
  - `PUT /put/{id}`: Update a single todo item.
  - `POST /create/{id}`: Create a new todo item.
  - `DELETE /delete/{id}`: Delete a todo item.

### AuthController
- **User Registration and Login APIs**
- **Role-based Access Control**
  - **User**: Can only access `GET /getall` to get the list of todo items. All other API calls will return a `HTTP 401: Unauthorized` error.
  - **Admin**: Has access to all the APIs in `TodoController`.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- SQL Server
- Git
- Heroku CLI (for deployment)

### Installation Steps

1. **Clone the repository**
<!-- 
   ```bash
   git clone https://github.com/yourusername/yourprojectname.git
   cd yourprojectname -->
