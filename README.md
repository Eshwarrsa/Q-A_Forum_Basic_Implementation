# Q&A Forum

A simple Question and Answer forum web application built with Django, where users can register, log in, ask questions, and provide answers.

## Features

- User Registration and Login
- Secure authentication with Django's built-in `User` model
- Ask and Answer questions
- View a list of all questions and their details
- Add answers to specific questions
- Basic UI for easy navigation

## Requirements

- Python 3.8 or higher
- Django 5.1.4
- SQLite (default database)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Eshwarrsa/Q-A_Forum_Basic_Implementation.git
    cd Q-A_Forum_Basic_Implementation
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Open the application in your browser at `http://127.0.0.1:8000`.

## Usage

### 1. Register and Login
- Navigate to `/accounts/register/` to create a new account.
- Log in at `/accounts/login/`.

### 2. Ask a Question
- After logging in, click the **Ask a Question** link.
- Fill in the form and submit your question.

### 3. Answer Questions
- View a question's details by clicking on it from the homepage.
- Use the **Add an Answer** link to submit your answer.

### 4. View All Questions
- The homepage (`/`) lists all questions ordered by the most recently added.

## Directory Structure

```
qa-forum/
├── forum/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── QandAForum/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
│   ├── base.html
│   ├── question_list.html
│   ├── question_detail.html
│   ├── add_question.html
│   ├── add_answer.html
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Dependencies

- Django 5.1.4

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Settings

### Database
By default, the project uses SQLite. You can change the database in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```