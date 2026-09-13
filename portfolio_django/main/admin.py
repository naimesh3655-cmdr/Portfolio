from django.contrib import admin
from .models import Focus, Goal, Interest, Journey, PortfolioProfile, Project, Skill


@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identity & Hero", {"fields": ("name", "tagline", "hero_intro", "hero_note")}),
        ("About Me", {"fields": ("about_intro", "about_story", "about_building", "about_data", "quote")}),
        ("Education", {"fields": ("college", "degree", "specialization", "year")}),
        ("Links & Contact", {"fields": ("github_link", "linkedin_link", "contact_text")}),
    )

    def has_add_permission(self, request):
        return not PortfolioProfile.objects.exists()


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "order")
    list_editable = ("order",)
    search_fields = ("year", "title", "description")


@admin.register(Focus)
class FocusAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "order")
    list_editable = ("order",)


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ("icon", "title", "order")
    list_editable = ("order",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "order", "created_at")
    list_editable = ("featured", "order")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "short_description", "description", "tech_stack")
    list_filter = ("featured",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "order")
    list_editable = ("order",)
    list_filter = ("category",)
    search_fields = ("name",)
