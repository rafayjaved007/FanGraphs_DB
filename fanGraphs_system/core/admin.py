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


admin.site.register(Team, TeamAdmin)
admin.site.register(Schedule, ScheduleAdmin)
