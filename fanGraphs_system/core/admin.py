from django.contrib import admin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('name', 'league', 'division')
    list_filter = ['league', 'division']
    search_fields = ['name',]


class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    list_display = ('team', 'opp', 'w_or_l')
    list_filter = ['w_or_l',]
    search_fields = ['team__name',]

    def team(self, obj):
        return str(obj.team.name)


class PitcherAdmin(admin.ModelAdmin):
    model = Pitcher
    list_display = ('team', 'player', 'role')
    list_filter = ['role',]
    search_fields = ['team__name', 'player']

    def team(self, obj):
        return str(obj.team.name)


class PitchersStandardAdmin(admin.ModelAdmin):
    model = PitchersStandard
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class PitchersAdvancedAdmin(admin.ModelAdmin):
    model = PitchersAdvanced
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class PitchersWinProbabilityAdmin(admin.ModelAdmin):
    model = PitchersWinProbability
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class DualHittersWinProbabilityAdmin(admin.ModelAdmin):
    model = DualHittersWinProbability
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class PitchersPlateDisciplineAdmin(admin.ModelAdmin):
    model = PitchersStandard
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class HitterAdmin(admin.ModelAdmin):
    model = Hitter
    list_display = ('team', 'player', 'role')
    list_filter = ['role',]
    search_fields = ['team__name', 'player']

    def team(self, obj):
        return str(obj.team.name)


class HittersStandardAdmin(admin.ModelAdmin):
    model = HittersStandard
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class HittersAdvancedAdmin(admin.ModelAdmin):
    model = HittersAdvanced
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class HittersPlateDisciplineAdmin(admin.ModelAdmin):
    model = HittersStandard
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class DualHittersStandardAdmin(admin.ModelAdmin):
    model = DualHittersStandard
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class DualHittersAdvancedAdmin(admin.ModelAdmin):
    model = DualHittersAdvanced
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


class DualHittersPlateDisciplineAdmin(admin.ModelAdmin):
    model = DualHittersStandard
    list_display = ('date', 'player', 'team_name', 'opp')
    list_filter = ['date',]
    search_fields = ['team_name__name', 'player__player', 'opp']

    def player(self, obj):
        return str(obj.player.player)

    def team_name(self, obj):
        return str(obj.team_name.name)


admin.site.register(Team, TeamAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Pitcher, PitcherAdmin)
admin.site.register(PitchersStandard, PitchersStandardAdmin)
admin.site.register(PitchersAdvanced, PitchersAdvancedAdmin)
admin.site.register(PitchersWinProbability, PitchersWinProbabilityAdmin)
admin.site.register(PitchersPlateDiscipline, PitchersPlateDisciplineAdmin)
admin.site.register(Hitter, HitterAdmin)
admin.site.register(HittersStandard, HittersStandardAdmin)
admin.site.register(HittersAdvanced, HittersAdvancedAdmin)
admin.site.register(HittersPlateDiscipline, HittersPlateDisciplineAdmin)
admin.site.register(DualHittersStandard, DualHittersStandardAdmin)
admin.site.register(DualHittersAdvanced, DualHittersAdvancedAdmin)
admin.site.register(DualHittersWinProbability, DualHittersWinProbabilityAdmin)
admin.site.register(DualHittersPlateDiscipline, DualHittersPlateDisciplineAdmin)
