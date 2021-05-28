from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('schedule', ScheduleViewSet)
router.register('team', TeamViewSet)

urlpatterns = []

urlpatterns += router.urls
