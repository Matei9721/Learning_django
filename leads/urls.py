from rest_framework import routers
from .api import LeadViewSet, MovieViewSet,CountriesViewSet

router = routers.DefaultRouter()
router.register(r'api/leads', LeadViewSet, 'leads')
router.register(r'api/movies', MovieViewSet, 'movies')
router.register(r'api/countries', CountriesViewSet, 'countries')

urlpatterns = router.urls

