# Portfolio (Django)

## Setup
    python -m venv venv
    source venv/bin/activate        # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Visit http://127.0.0.1:8000/ for the site, http://127.0.0.1:8000/admin/ to add
Projects and Skills.

## Where things live
- `main/models.py`      -> Project, Skill models
- `main/templates/main/` -> base.html, home.html, project_detail.html
- `main/static/main/`   -> style.css, script.js (AOS scroll-reveal init)

## Adding a project
Go to /admin/, add a Project (title, slug, description, tech_stack, image,
github_link). It shows up on the home page automatically, newest/ordered
first. Set `featured=True` and a low `order` value to pin it near the top.

## Scroll animations
Any element with `data-aos="fade-up"` (or fade-right/zoom-in/etc, see
https://michalsnik.github.io/aos/) animates in the first time it's scrolled
into view. `AOS.init()` lives in main/static/main/js/script.js.

## Deploying
This is a normal Django project — deploy on Railway, Render, PythonAnywhere,
or a VPS. Before going live: set DEBUG=False, set ALLOWED_HOSTS, move
SECRET_KEY to an environment variable, and set up static/media file serving
(whitenoise for static, S3/Cloudinary for media in production).
