from .models import *
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name',]


class ScheduleSerializer(serializers.ModelSerializer):
    team = serializers.CharField(max_length=100)

    class Meta:
        model = Schedule
        fields = '__all__'

    def validate(self, attr):
        attr['team'] = Team.objects.get(name=attr['team'])
        return attr


class PitcherSerializer(serializers.ModelSerializer):
    team = serializers.CharField(max_length=100)

    class Meta:
        model = Pitcher
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team'] = Team.objects.get(name=attr['team'])
        return attr


class PitchersStandardSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(max_length=100)
    player = serializers.CharField(max_length=100)

    class Meta:
        model = PitchersStandard
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team_name'] = Team.objects.get(name=attr['team_name'])
        attr['player'] = Pitcher.objects.get(player=attr['player'])
        return attr


class PitchersAdvancedSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(max_length=100)
    player = serializers.CharField(max_length=100)

    class Meta:
        model = PitchersAdvanced
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team_name'] = Team.objects.get(name=attr['team_name'])
        attr['player'] = Pitcher.objects.get(player=attr['player'])
        return attr


class PitchersWinProbabilitySerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(max_length=100)
    player = serializers.CharField(max_length=100)

    class Meta:
        model = PitchersWinProbability
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team_name'] = Team.objects.get(name=attr['team_name'])
        attr['player'] = Pitcher.objects.get(player=attr['player'])
        return attr


class PitchersPlateDisciplineSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(max_length=100)
    player = serializers.CharField(max_length=100)

    class Meta:
        model = PitchersPlateDiscipline
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team_name'] = Team.objects.get(name=attr['team_name'])
        attr['player'] = Hitter.objects.get(player=attr['player'])
        return attr


class HitterSerializer(serializers.ModelSerializer):
    team = serializers.CharField(max_length=100)

    class Meta:
        model = Hitter
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team'] = Team.objects.get(name=attr['team'])
        return attr


class HittersStandardSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(max_length=100)
    player = serializers.CharField(max_length=100)

    class Meta:
        model = HittersStandard
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team_name'] = Team.objects.get(name=attr['team_name'])
        attr['player'] = Hitter.objects.get(player=attr['player'])
        return attr


class HittersAdvancedSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(max_length=100)
    player = serializers.CharField(max_length=100)

    class Meta:
        model = HittersAdvanced
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team_name'] = Team.objects.get(name=attr['team_name'])
        attr['player'] = Hitter.objects.get(player=attr['player'])
        return attr


class HittersPlateDisciplineSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(max_length=100)
    player = serializers.CharField(max_length=100)

    class Meta:
        model = HittersPlateDiscipline
        fields = '__all__'
        depth = 1

    def validate(self, attr):
        attr['team_name'] = Team.objects.get(name=attr['team_name'])
        attr['player'] = Hitter.objects.get(player=attr['player'])
        return attr