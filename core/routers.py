from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'pages', views.PagesViewSet, basename="pages")
router.register(r'projects', views.ProjectsViewSet, basename="projects")

urlpatterns = router.urls