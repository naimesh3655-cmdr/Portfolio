from django.db import migrations


def seed_portfolio(apps, schema_editor):
    Profile = apps.get_model("main", "PortfolioProfile")
    Journey = apps.get_model("main", "Journey")
    Focus = apps.get_model("main", "Focus")
    Goal = apps.get_model("main", "Goal")
    Interest = apps.get_model("main", "Interest")
    Skill = apps.get_model("main", "Skill")

    if not Profile.objects.exists():
        Profile.objects.create(
            name="Naimesh Padhi",
            tagline="Learning by building.",
            hero_intro="A curious CSE student at SRM Institute of Science and Technology, specializing in Data Science and Business Systems and turning ideas into practical software.",
            hero_note="Currently learning, building, breaking, fixing, and shipping projects that help me become a better engineer.",
            about_intro="I'm a 2nd-year Computer Science and Engineering student at SRM Institute of Science and Technology, specializing in Data Science and Business Systems.",
            about_story="I'm building my foundation through programming, data structures and algorithms, OOP, databases, backend development, and practical projects. I enjoy taking an idea that feels complicated at first and turning it into something structured, understandable, and useful.",
            about_building="Projects are where I connect what I learn in class with problems that could actually be useful outside the classroom.",
            about_data="My DSBS specialization is pushing me toward data science, analytics, machine learning, and practical AI applications.",
            quote="I'm still learning — and that's exactly what makes this part of the journey exciting.",
            college="SRM Institute of Science and Technology",
            degree="Computer Science & Engineering",
            specialization="Data Science and Business Systems",
            year="2nd Year",
            github_link="https://github.com/naimesh3655-cmdr",
            linkedin_link="https://www.linkedin.com/in/naimesh-padhi-186163326/",
            contact_text="I'm always open to learning, collaborating, and talking about software, data, and projects.",
        )

    if not Journey.objects.exists():
        Journey.objects.bulk_create([
            Journey(year="2024", title="Started my CSE journey", description="Began exploring computer science, programming, and the fundamentals that make software work.", order=1),
            Journey(year="2025", title="Strengthened programming fundamentals", description="Spent more time with OOP, DSA, problem solving, databases, and learning how to build projects rather than only solve exercises.", order=2),
            Journey(year="2026", title="Building real projects", description="Working on ideas such as BloodLink, AgriLink, and other applications while learning backend development and better software structure.", order=3),
            Journey(year="Next", title="Step into the industry", description="Build a stronger portfolio, contribute to real projects, and become ready for meaningful internship opportunities.", order=4),
        ])

    if not Focus.objects.exists():
        Focus.objects.bulk_create([
            Focus(icon="🧠", title="DSA & problem solving", description="Getting stronger at data structures, algorithms, logic, and writing solutions that are both correct and efficient.", order=1),
            Focus(icon="🗄️", title="Backend & databases", description="Learning Django, SQL, database design, APIs, and how the pieces of a real application fit together.", order=2),
            Focus(icon="📊", title="Data Science", description="Exploring analytics, Python data tools, machine learning, and the practical side of working with data.", order=3),
        ])

    if not Goal.objects.exists():
        Goal.objects.bulk_create([
            Goal(number="01", title="Strong fundamentals", description="Get genuinely good at DSA, programming concepts, and writing clean, maintainable code.", order=1),
            Goal(number="02", title="Build real systems", description="Turn project ideas into useful applications with solid backend and database foundations.", order=2),
            Goal(number="03", title="Explore Data Science", description="Grow from using data to understanding it — analytics, machine learning, and practical AI applications.", order=3),
            Goal(number="04", title="Become internship-ready", description="Build a strong body of work, contribute to real projects, and learn from experienced developers.", order=4),
        ])

    if not Interest.objects.exists():
        Interest.objects.bulk_create([
            Interest(icon="📚", title="Learning", description="I enjoy going down rabbit holes when a topic catches my attention and understanding the why behind it.", order=1),
            Interest(icon="💡", title="Ideas & experiments", description="Small ideas often become the best way to learn a new technology or understand a problem from a different angle.", order=2),
            Interest(icon="🚀", title="Building", description="I like seeing an idea move from a rough thought to something I can actually run, test, and improve.", order=3),
        ])

    if not Skill.objects.exists():
        Skill.objects.bulk_create([
            Skill(name="Java", category="language", order=1), Skill(name="Python", category="language", order=2), Skill(name="C", category="language", order=3),
            Skill(name="HTML", category="frontend", order=1), Skill(name="CSS", category="frontend", order=2), Skill(name="JavaScript", category="frontend", order=3),
            Skill(name="Django", category="backend", order=1), Skill(name="SQL", category="backend", order=2), Skill(name="SQLite", category="backend", order=3),
            Skill(name="Pandas", category="data", order=1), Skill(name="NumPy", category="data", order=2), Skill(name="Data Analysis", category="data", order=3),
            Skill(name="Git", category="tools", order=1), Skill(name="GitHub", category="tools", order=2), Skill(name="VS Code", category="tools", order=3),
        ])


def unseed(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("main", "0002_portfolio_cms")]
    operations = [migrations.RunPython(seed_portfolio, unseed)]
