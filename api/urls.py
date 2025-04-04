from django.urls import path, include
from .views import ProtectedView
from rest_framework.routers import DefaultRouter
from .views import ProtectedView, UserViewSet, CountriesViewSet, StatesViewSet, CitiesViewSet, CountriesInfoViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'countries', CountriesViewSet)
router.register(r'regions', StatesViewSet)
router.register(r'cities', CitiesViewSet)
router.register(r'country-info', CountriesInfoViewSet)

urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('access/', include(router.urls)),
]
