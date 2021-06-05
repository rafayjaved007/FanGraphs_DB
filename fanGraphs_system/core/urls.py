from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('schedule', ScheduleViewSet)
router.register('hitters', HitterViewSet)
router.register('hitters-standard', HittersStandardViewSet)
router.register('hitters-advanced', HittersAdvancedViewSet)
router.register('hitters-plate-discipline', HittersPlateDisciplineViewSet)
router.register('pitchers', PitcherViewSet)
router.register('pitchers-standard', PitchersStandardViewSet)
router.register('pitchers-advanced', PitchersAdvancedViewSet)
router.register('pitchers-win-probability', PitchersWinProbabilityViewSet)
router.register('pitchers-plate-discipline', PitchersPlateDisciplineViewSet)
router.register('teams', TeamViewSet)

urlpatterns = []

urlpatterns += router.urls
