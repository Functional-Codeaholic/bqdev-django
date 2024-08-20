from django.contrib import admin

# Register your models here.
from .models import (
    Pages, Projects
)

class PagesInline(admin.StackedInline):
    model = Pages
    extra = 1
    
class ProjectsInline(admin.StackedInline):
    model = Projects
    extra = 1
    
@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'h1')
    
    def get_pages(self, obj):
        return obj.pages.title
    get_pages.short_description = "Pages"
    
    
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client_name', 'client_description', 'project_goal', 'experience', 'outcome', 'screenshot', 'project_url')
    
    def get_projects(self, obj):
        return obj.projects.title
    get_projects.short_description = "Projects"
    