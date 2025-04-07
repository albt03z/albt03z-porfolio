from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProtectedView, UserViewSet, CountriesViewSet, StatesViewSet, CountriesInfoViewSet, ContinentsViewSet, TypesDocumentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'countries', CountriesViewSet)
router.register(r'states', StatesViewSet)
router.register(r'countries-info', CountriesInfoViewSet)
router.register(r'continents', ContinentsViewSet)
router.register(r'types-document', TypesDocumentViewSet)

urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('access/', include(router.urls)),
]
