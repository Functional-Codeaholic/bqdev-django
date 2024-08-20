from rest_framework import serializers
from .models import Pages, Projects

class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ['id', 'name', 'h1']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'project_name', 'client_name', 'client_description', 'project_goal', 'experience', 'outcome', 'screenshot', 'project_url']