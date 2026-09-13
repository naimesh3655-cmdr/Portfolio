from django.db import migrations
from django.contrib.auth.hashers import make_password


def seed(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    User = apps.get_model('auth', 'User')

    projects = [
        {
            'title': 'BloodLink', 'slug': 'bloodlink',
            'short_description': 'A blood donor and blood bank platform designed to make finding and coordinating blood support easier.',
            'description': 'BloodLink is a project focused on connecting people who need blood with donors and blood-bank information. The project is an opportunity to learn application architecture, databases, authentication, CRUD workflows, and how technology can solve a practical problem.',
            'tech_stack': 'Python, Django, SQLite, HTML, CSS, JavaScript', 'featured': True, 'order': 1,
        },
        {
            'title': 'AgriLink', 'slug': 'agrilink',
            'short_description': 'A technology-driven agriculture platform built around useful information and connections for the farming ecosystem.',
            'description': 'AgriLink is a project exploring how software can help organize agriculture-related information and services. It is part of my journey toward building practical applications rather than only classroom exercises.',
            'tech_stack': 'Python, Django, HTML, CSS, JavaScript, SQL', 'featured': True, 'order': 2,
        },
        {
            'title': 'Chatting App', 'slug': 'chatting-app',
            'short_description': 'A messaging application built to explore user interaction, backend logic, and communication between clients and a server.',
            'description': 'This project explores the foundations behind a chat application: users, messages, application state, backend logic, and a responsive interface. It is a practical way to understand how a feature grows from an idea into a working system.',
            'tech_stack': 'Python, Django, JavaScript, HTML, CSS, SQLite', 'featured': True, 'order': 3,
        },
    ]
    for data in projects:
        Project.objects.get_or_create(slug=data['slug'], defaults=data)

    # Create a convenient development/admin account only if it does not already exist.
    # Change this password immediately after first login.
    if not User.objects.filter(username='portfolio_admin').exists():
        User.objects.create(
            username='portfolio_admin',
            email='naimesh3655@gmail.com',
            password=make_password('Naimesh@123'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )


def unseed(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [('main', '0003_seed_portfolio')]
    operations = [migrations.RunPython(seed, unseed)]
