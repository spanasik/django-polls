from models import *
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('title', 'user')
    ordering = ['pub_date']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',),}
    fields = (
        (None, {
            'fields': ('title', 'description', 'user', 'ip_address')
        }),
        (_('Advanced settings'), {
            'classes': 'collapse',
            'fields' : ('state', 'slug', 'pub_date')
        }),
    )

admin.site.register(Poll, PollAdmin)

class VoteAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('poll', 'choice', 'user')
    ordering = ['pub_date']
    search_fields = ['poll']
    radio_fields = {"choice": admin.VERTICAL}
    fields = (
        (None, {
            'fields': ('poll', 'choice', 'user', 'ip_address')
        }),
        (_('Advanced settings'), {
            'classes': 'collapse',
            'fields' : ('pub_date', )
        }),
    )

admin.site.register(Vote, VoteAdmin)