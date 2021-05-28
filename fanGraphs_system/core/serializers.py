from .models import *
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name',]


class ScheduleSerializer(serializers.ModelSerializer):
    # w_or_l = serializers.CharField()
    team = serializers.CharField(max_length=100)

    class Meta:
        model = Schedule
        fields = '__all__'

    def validate(self, attr):
        attr['team'] = Team.objects.get(name=attr['team'])
        return attr
