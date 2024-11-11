from rest_framework import routers
from .api import UsersViewSet, ObservationsViewSet, StationsViewSet, SensorsViewSet, UserLocationViewSet, MeetingViewSet, ModelosPrediccionViewSet

router = routers.DefaultRouter()

router.register('api/users', UsersViewSet, 'users')

router.register('api/observations', ObservationsViewSet, 'observations')

router.register('api/stations', StationsViewSet, 'stations')

router.register('api/sensors', SensorsViewSet, 'sensors')

router.register('api/userlocation', UserLocationViewSet, 'userlocation')

router.register('api/meetingpoint', MeetingViewSet, 'meetingpoint')

router.register('api/modelosprediccion', ModelosPrediccionViewSet, 'modelosprediccion')

urlpatterns = router.urls