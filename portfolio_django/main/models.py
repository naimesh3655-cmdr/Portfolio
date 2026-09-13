from django.db import models


class PortfolioProfile(models.Model):
    name = models.CharField(max_length=100, default="Naimesh Padhi")
    tagline = models.CharField(max_length=180, default="Learning by building.")
    hero_intro = models.TextField(
        default="A curious CSE student at SRM Institute of Science and Technology, specializing in Data Science and Business Systems."
    )
    hero_note = models.TextField(
        default="Currently learning, building, breaking, fixing, and shipping projects that help me become a better engineer."
    )
    about_intro = models.TextField(blank=True)
    about_story = models.TextField(blank=True)
    about_building = models.TextField(blank=True)
    about_data = models.TextField(blank=True)
    quote = models.CharField(max_length=300, blank=True)
    college = models.CharField(max_length=180, default="SRM Institute of Science and Technology")
    degree = models.CharField(max_length=120, default="Computer Science & Engineering")
    specialization = models.CharField(max_length=150, default="Data Science and Business Systems")
    year = models.CharField(max_length=50, default="2nd Year")
    github_link = models.URLField(default="https://github.com/naimesh3655-cmdr")
    linkedin_link = models.URLField(default="https://www.linkedin.com/in/naimesh-padhi-186163326/")
    contact_text = models.TextField(
        default="I'm always open to learning, collaborating, and talking about software, data, and projects."
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio Profile"
        verbose_name_plural = "Portfolio Profile"

    def __str__(self):
        return self.name


class Journey(models.Model):
    year = models.CharField(max_length=40)
    title = models.CharField(max_length=120)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name_plural = "Journey"

    def __str__(self):
        return f"{self.year} — {self.title}"


class Focus(models.Model):
    icon = models.CharField(max_length=10, default="→")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Current Focus"
        verbose_name_plural = "Current Focus"

    def __str__(self):
        return self.title


class Goal(models.Model):
    number = models.CharField(max_length=10, default="01")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Interest(models.Model):
    icon = models.CharField(max_length=10, default="✦")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="Used in the URL, e.g. bloodlink")
    short_description = models.CharField(max_length=200, help_text="One-liner shown on the card")
    description = models.TextField(help_text="Full write-up shown on the detail page")
    tech_stack = models.CharField(max_length=200, help_text="Comma-separated, e.g. Python, Django, SQLite")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Show as a featured project")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("language", "Languages"),
        ("frontend", "Frontend"),
        ("backend", "Backend / Systems"),
        ("data", "Data Science"),
        ("tools", "Tools"),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "id"]

    def __str__(self):
        return self.name
