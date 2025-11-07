# Online Course Portal

## Overview

I built this online learning platform as a Django-based web application that enables students to discover and enroll in courses while giving instructors and administrators complete control over course management.

## What I Implemented

### For Students
- **Account Management**: Created user registration and authentication system
- **Course Discovery**: Implemented browsing functionality to explore available courses
- **Enrollment System**: Designed enrollment feature to join courses with a single click
- **Learning Interface**: Built pages to access video lectures and course materials

### For Administrators
- **Content Management**: Developed admin panel to create, edit, and remove courses
- **User Oversight**: Added user management capabilities
- **Enrollment Tracking**: Implemented enrollment monitoring dashboard
- **Discussion Features**: Included optional comment and discussion sections

## Technologies I Used

I chose the following stack for this project:

- **Frontend Layer**: HTML5, CSS3, Bootstrap 5 for responsive design, and vanilla JavaScript
- **Backend Framework**: Django (Python) for robust server-side logic
- **Data Storage**: SQLite database for development simplicity

## Getting Started

Follow these steps to run the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/online-course-portal.git
cd online-course-portal
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# source venv/bin/activate    # On macOS/Linux
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
python manage.py migrate
```

### 5. Create Admin Account
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your administrator credentials.

### 6. Launch Development Server
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`

## Project Structure

The application follows Django's standard project layout with separate apps for courses, users, and enrollments.

## Future Enhancements

I plan to add:
- Payment integration for paid courses
- Certificate generation upon course completion
- Progress tracking for enrolled students
- Quiz and assignment features
- Email notifications for course updates

## Contributing

Feel free to fork this repository and submit pull requests. I'm open to suggestions and improvements!

## License

This project is available for educational purposes.
