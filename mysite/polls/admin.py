from django.contrib import admin
from polls.models import Choice, Poll, PollingLocation

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class LocationInline (admin.TabularInline):
    model = PollingLocation.polls.through

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline,LocationInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

class LocationAdmin(admin.ModelAdmin):
    inlines = [LocationInline]
    exclude = ('questions')

admin.site.register(Poll, PollAdmin)
admin.site.register(PollingLocation)

