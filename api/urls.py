from django.urls import path, include
from .views import ProtectedView
from rest_framework.routers import DefaultRouter
from .views import ProtectedView, UserViewSet, CountryViewSet, RegionViewSet, CityViewSet, CountryInfoViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'cities', CityViewSet)
router.register(r'country-info', CountryInfoViewSet)

urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('access/', include(router.urls)),
]
