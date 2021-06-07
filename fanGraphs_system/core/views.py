from rest_framework import viewsets
from .serializers import *


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class PitcherViewSet(viewsets.ModelViewSet):
    queryset = Pitcher.objects.all()
    serializer_class = PitcherSerializer


class PitchersStandardViewSet(viewsets.ModelViewSet):
    queryset = PitchersStandard.objects.all()
    serializer_class = PitchersStandardSerializer


class PitchersAdvancedViewSet(viewsets.ModelViewSet):
    queryset = PitchersAdvanced.objects.all()
    serializer_class = PitchersAdvancedSerializer


class PitchersWinProbabilityViewSet(viewsets.ModelViewSet):
    queryset = PitchersWinProbability.objects.all()
    serializer_class = PitchersWinProbabilitySerializer


class PitchersPlateDisciplineViewSet(viewsets.ModelViewSet):
    queryset = PitchersPlateDiscipline.objects.all()
    serializer_class = PitchersPlateDisciplineSerializer


class HitterViewSet(viewsets.ModelViewSet):
    queryset = Hitter.objects.all()
    serializer_class = HitterSerializer


class HittersStandardViewSet(viewsets.ModelViewSet):
    queryset = HittersStandard.objects.all()
    serializer_class = HittersStandardSerializer


class HittersAdvancedViewSet(viewsets.ModelViewSet):
    queryset = HittersAdvanced.objects.all()
    serializer_class = HittersAdvancedSerializer


class HittersPlateDisciplineViewSet(viewsets.ModelViewSet):
    queryset = HittersPlateDiscipline.objects.all()
    serializer_class = HittersPlateDisciplineSerializer


class DualHittersStandardViewSet(viewsets.ModelViewSet):
    queryset = DualHittersStandard.objects.all()
    serializer_class = DualHittersStandardSerializer


class DualHittersAdvancedViewSet(viewsets.ModelViewSet):
    queryset = DualHittersAdvanced.objects.all()
    serializer_class = DualHittersAdvancedSerializer


class DualHittersWinProbabilityViewSet(viewsets.ModelViewSet):
    queryset = DualHittersWinProbability.objects.all()
    serializer_class = DualHittersWinProbabilitySerializer


class DualHittersPlateDisciplineViewSet(viewsets.ModelViewSet):
    queryset = DualHittersPlateDiscipline.objects.all()
    serializer_class = DualHittersPlateDisciplineSerializer
