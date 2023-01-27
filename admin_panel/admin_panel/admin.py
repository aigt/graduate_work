from django.contrib import admin

from .models import Subscribers


@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'subsciber_status', 'subsciber_status', 'date_subsctibe')

