from django.urls import path, include
from .routers import router, DefaultRouter
from .views import ProjectsViewSet, PagesViewSet

router = DefaultRouter()

router.register(r'pages', PagesViewSet, basename="pages")
router.register(r'projects', ProjectsViewSet, basename="projects")

urlpatterns = [
    path('', include(router.urls)),
]
