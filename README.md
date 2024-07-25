# Tech Event Listings - A Wagtail CMS Project

## Project Demo Video

https://github.com/user-attachments/assets/06eb0aa9-71bd-4c9b-a3a8-4792c0631ae7



## About

Tech Event Listings is a web application built with Wagtail CMS that allows users to explore and manage tech community events.

## Features

- **Home Page**: A welcoming landing page introducing latest events.
- **Event Listings**: A page displaying all upcoming events.
- **Detailed Event Pages**: Individual pages for each event, including:
  - Header image
  - Start and end times
  - Venue information
  - Detailed event description
  - Pricing details
  - Registration link
  - Event capacity
- **Search Functionality**: Allows users to find events quickly.
- **Tagging System**: Events can be categorized and filtered using tags (implemented with django-taggit).

## Technologies Used

- Wagtail CMS
- Django
- Python
- Tailwind CSS
- django-taggit (for tagging functionality)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/Daksh777/eventlistings
   cd eventlistings
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the admin panel at `http://localhost:8000/admin` and start adding events!
