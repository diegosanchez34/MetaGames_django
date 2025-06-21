# MetaGames

MetaGames is a web platform built with Django that allows users to manage and download video games, as well as handle user administration and contact the support team.

## Features

- Browse and download video games by categories (New, Classic, Retro).
- Admin panel for CRUD operations on games.
- User registration and login.
- Contact form with validations.
- Modern and responsive interface using Bootstrap and custom CSS.

## Technologies Used

- Python 3
- Django
- SQLite (default, can be changed)
- Bootstrap 5
- HTML5 & CSS3
- JavaScript

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your_user/MetaGames_django.git
   cd MetaGames_django
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional):**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the server:**
   ```sh
   python manage.py runserver
   ```

## Usage

- Access the web app at `http://127.0.0.1:8000/`.
- Browse sections: games list, registration, contact, admin, etc.
- The admin panel is available at `/crud/` (requires permissions).

## Credits

Developed by Diego Sanchez, David Coo, Nicolas Carcamo.

---

Feel free to contribute or report issues!
