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
