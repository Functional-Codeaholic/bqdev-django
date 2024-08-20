import copy
from .models import Projects, Pages
from .serializers import PagesSerializer, ProjectsSerializer
from rest_framework.permissions import DjangoModelPermissions, AllowAny
from rest_framework import viewsets
# Create your views here.

class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)
        # Block Get access without view perms
        self.perms_map["GET"] = ["%(app_label)s.view_%(model_name)s"]
        
class PagesViewSet(viewsets.ModelViewSet):
    serializer_class = PagesSerializer
    permission_classes = (CustomDjangoModelPermissions,)
    
    def get_queryset(self):
        return Pages.objects.all()
        
class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Projects.objects.all()