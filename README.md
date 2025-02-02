# FAQ API Project

This project is a Django-based API for managing Frequently Asked Questions (FAQ). It provides multilingual support, integrates a WYSIWYG editor, and uses Redis for caching to optimize performance. The API serves FAQ data in multiple languages, and the data is cached to improve response times.

## Features
- Multilingual FAQ support (English, Hindi, Bengali)
- WYSIWYG editor integration for rich text content
- API to fetch FAQs using Django Rest Framework
- Redis caching for improved performance

## Installation

Follow the steps below to get this project up and running locally.

### Prerequisites
- Python 3.x
- Redis (for caching)
- pip (Python package installer)

### 1. Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/faq-project.git
cd faq-project
```
### 2. Set Up a Virtual Environment
Create and activate a virtual environment for the project:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### 3. Install Dependencies
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
### 4. Set Up Database
Make sure your database is set up and migrate the models:

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)
Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```
### 6. Run the Server
Start the Django development server:

```bash
python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/api/faqs/.
