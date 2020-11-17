from rest_framework import routers
from .api import LeadViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/movies', MovieViewSet, 'movies')

urlpatterns = router.urls

