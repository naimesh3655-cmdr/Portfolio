from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("main", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="PortfolioProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="Naimesh Padhi", max_length=100)),
                ("tagline", models.CharField(default="Learning by building.", max_length=180)),
                ("hero_intro", models.TextField(default="A curious CSE student at SRM Institute of Science and Technology, specializing in Data Science and Business Systems.")),
                ("hero_note", models.TextField(default="Currently learning, building, breaking, fixing, and shipping projects that help me become a better engineer.")),
                ("about_intro", models.TextField(blank=True)),
                ("about_story", models.TextField(blank=True)),
                ("about_building", models.TextField(blank=True)),
                ("about_data", models.TextField(blank=True)),
                ("quote", models.CharField(blank=True, max_length=300)),
                ("college", models.CharField(default="SRM Institute of Science and Technology", max_length=180)),
                ("degree", models.CharField(default="Computer Science & Engineering", max_length=120)),
                ("specialization", models.CharField(default="Data Science and Business Systems", max_length=150)),
                ("year", models.CharField(default="2nd Year", max_length=50)),
                ("github_link", models.URLField(default="https://github.com/naimesh3655-cmdr")),
                ("linkedin_link", models.URLField(default="https://www.linkedin.com/in/naimesh-padhi-186163326/")),
                ("contact_text", models.TextField(default="I'm always open to learning, collaborating, and talking about software, data, and projects.")),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Portfolio Profile", "verbose_name_plural": "Portfolio Profile"},
        ),
        migrations.CreateModel(
            name="Journey",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("year", models.CharField(max_length=40)),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField()),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"], "verbose_name_plural": "Journey"},
        ),
        migrations.CreateModel(
            name="Focus",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("icon", models.CharField(default="→", max_length=10)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"], "verbose_name": "Current Focus", "verbose_name_plural": "Current Focus"},
        ),
        migrations.CreateModel(
            name="Goal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.CharField(default="01", max_length=10)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="Interest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("icon", models.CharField(default="✦", max_length=10)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.AlterField(
            model_name="skill",
            name="category",
            field=models.CharField(choices=[("language", "Languages"), ("frontend", "Frontend"), ("backend", "Backend / Systems"), ("data", "Data Science"), ("tools", "Tools")], max_length=20),
        ),
        migrations.AlterField(
            model_name="skill",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterModelOptions(
            name="skill",
            options={"ordering": ["category", "order", "id"]},
        ),
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["order", "-created_at"]},
        ),
    ]
