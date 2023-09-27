from django.contrib import admin
from .models import Survey, Option, Vote

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline_date', 'is_open', 'creation_date', 'edit_date')
    ordering = ('-id',)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Option)
admin.site.register(Vote)
