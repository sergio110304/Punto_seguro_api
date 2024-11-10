from rest_framework import routers
from .api import UsersViewSet, ObservationsViewSet, StationsViewSet, SensorsViewSet

router = routers.DefaultRouter()

router.register('api/users', UsersViewSet, 'users')

router.register('api/observations', ObservationsViewSet, 'observations')

router.register('api/stations', StationsViewSet, 'stations')

router.register('api/sensors', SensorsViewSet, 'sensors')

urlpatterns = router.urls