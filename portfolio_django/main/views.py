from itertools import groupby
from operator import attrgetter

from django.shortcuts import get_object_or_404, render

from .models import Focus, Goal, Interest, Journey, PortfolioProfile, Project, Skill


def home(request):
    profile = PortfolioProfile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    journey = Journey.objects.all()
    focuses = Focus.objects.all()
    goals = Goal.objects.all()
    interests = Interest.objects.all()

    labels = dict(Skill.CATEGORY_CHOICES)
    skills_by_category = [
        {"label": labels[category], "items": list(items)}
        for category, items in groupby(skills, key=attrgetter("category"))
    ]

    return render(request, "main/home.html", {
        "profile": profile,
        "projects": projects,
        "skills_by_category": skills_by_category,
        "journey": journey,
        "focuses": focuses,
        "goals": goals,
        "interests": interests,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "main/project_detail.html", {"project": project})
