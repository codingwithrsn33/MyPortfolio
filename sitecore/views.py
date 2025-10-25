from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail   # ✅ add this line
from django.conf import settings

def home(request):
    skills = [
        "Python", "Django", "Django REST Framework", "SQL",
        "MongoDB", "AWS", "Docker", "REST API",
        "React JS", "Git", "Postman"
    ]
    return render(request, 'sitecore/home.html', {'skills': skills})

def education(request):
    # Static education content
    education_list = [
        {
            'title': 'SSC',
            'institution': 'Kakasaheb Mhaske High School, AhilyaNagar',
            'score': '86.40%',
             
            'icon_class': 'fa-school'
        },
        {
            'title': 'HSC',
            'institution': 'Kakasaheb Mhaske Junior College, AhilyaNagar',
            'score': '91.17%',
             
            'icon_class': 'fa-school'
        },
        {
            'title': 'B.E. (Computer)',
            'institution': 'Sinhgad Academy of Engineering',
            'score': '7.80 CGPA',
             
            'icon_class': 'fa-graduation-cap'
        }
    ]
    return render(request, 'sitecore/education.html', {'education_list': education_list})

from django.shortcuts import render

def aboutme(request):
    personal_info = {
        'name': 'Rohan Subhash Darekar',
        'title': 'Python Developer | Backend Developer | Django | SQL | REST API',
        'experience': '1.4 Years of Experience',
        'phone': '+91-9075237180',
        'email': 'rohandarekar307@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/rohan-darekar-a865682a5/',
        'github': 'https://github.com/codingwithrsn33',
        'location': 'Pune, India',
        'summary': "Passionate Python Developer with 1.4 years of experience in designing and developing secure, scalable RESTful APIs using Django, MySQL, and MongoDB. Skilled in backend system integration, API design, and automation for cybersecurity and log monitoring solutions."
    }

    skills = [
        {'name': 'Python', 'level': 95},
        {'name': 'Django', 'level': 90},
        {'name': 'SQL / MySQL / MongoDB', 'level': 85},
        {'name': 'REST APIs', 'level': 90},
        {'name': 'Git / GitHub', 'level': 90},
        {'name': 'Data Structures & Algorithms', 'level': 85}
    ]

    experience_list = [
        {
            'role': 'Jr. Software Engineer',
            'company': 'I Cube IT System – Pune, India',
            'duration': 'Feb 2024 – May 2025',
            'details': [
                "Developed and maintained scalable RESTful APIs using Django 4.2 and DRF with JWT authentication.",
                "Integrated backend logic with PostgreSQL and MySQL; handled unstructured data with MongoDB.",
                "Automated periodic tasks using Linux CRON jobs, improving efficiency.",
                "Participated in Agile SDLC with cross-functional teams and international clients.",
                "Collaborated with senior engineers throughout the Software Development Lifecycle (SDLC) in Agile teams, participating in stand-ups, sprint planning, and code reviews.",
                "Applied OOP principles and modular design patterns to write clean, reusable, and testable Python code.",
                "Performed thorough unit testing and debugging using Postman, PyCharm, and Git, ensuring reliable deployments and API performance.",
                "Documented backend logic, API contracts, and database schema for internal use and cross-functional handovers." ,        ]
        }
    ]

    projects_list = [
        {
            'title': 'SecureCloud Integration Platform',
            'duration': 'May 2024 – April 2025',
           
            'technologies': 'Python (Django), REST APIs, JWT, CRON, MySQL, MongoDB, Git, Postman',
            'description': [
                "A cybersecurity-focused platform built for real-time log ingestion and threat detection. The application fetched logs from multiple external security sources, applied custom Python-based rules, and triggered alerts using a rule engine. It enhanced security visibility and automated alerting for the client."
            ]
        },
        {
            'title': 'Real-Time Chatting Application',
            'duration': 'Oct 2023 – Nov 2023',
            'technologies': 'Python, Socket Programming, Tkinter, SQLite, Threading, JSON',
            'description': [
                "desktop-based internal messaging application that simulates enterprise communication tools. It supports concurrent user connections, real-time two-way communication, and secure local data storage. Designed for seamless real-time chat using Python's built-in modules."
            ]
        }
    ]

     
    

    certifications_list = [
        'Python Training & Course Completion – IIT Bombay (Spoken Tutorial)',
        'Backend Development using Django – Udemy'
    ]

    achievements = [
        'Secured campus placement through performance and strong technical skills.',
        'Recognized as Top Performer in job readiness test during pre-placement training.'
    ]

    return render(request, 'sitecore/aboutme.html', {
        'personal_info': personal_info,
        'skills': skills,
        'experience_list': experience_list,
        'projects_list': projects_list,
        'certifications_list': certifications_list,
        'achievements': achievements
    })
 
def contact(request):
    return render(request, 'sitecore/contact.html')


