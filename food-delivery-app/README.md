# Food Delivery App

This project is a food delivery application similar to Uber Eats. It allows users to browse restaurants, create accounts, log in, and place orders for food delivery.

## Project Structure

```
food-delivery-app
├── manage.py
├── requirements.txt
├── .env
├── README.md
├── food_delivery
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps
│   ├── core
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates
│   │       └── core
│   │           ├── base.html
│   │           └── home.html
│   ├── accounts
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates
│   │       └── accounts
│   │           ├── login.html
│   │           ├── signup.html
│   │           └── profile_edit.html
│   ├── restaurants
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates
│   │       └── restaurants
│   │           └── search.html
│   ├── orders
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates
│   │       └── orders
│   │           └── confirm.html
│   └── api
│       ├── __init__.py
│       ├── views.py
│       └── urls.py
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── app.js
├── templates
│   └── includes
│       └── nav.html
└── tests
    ├── __init__.py
    └── test_basic.py
```

## Features

- **User Authentication**: Users can create accounts, log in, and edit their profiles.
- **Restaurant Search**: Users can search for restaurants and view their menus.
- **Order Placement**: Users can place orders and confirm their selections.
- **Responsive Design**: The application is designed to be mobile-friendly.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd food-delivery-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables in the `.env` file.

5. Run the migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the navigation bar to access different sections of the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.