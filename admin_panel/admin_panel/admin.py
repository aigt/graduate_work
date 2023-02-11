from django.contrib import admin

from .models import Payments, Subscribers  # noqa: WPS300


@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    """Класс для отображения модели Подписчика в админке."""

    list_display = ("id", "user_id", "subscriber_status", "date_subscribe")
    list_filter = ("subscriber_status",)
    search_fields = ("id",)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    """Класс для отображения модели Платежа в админке."""

    list_display = ("id", "user_id", "amount", "external_id", "external_payment", "refunded", "system_id")
    list_filter = ("refunded",)
    search_fields = ("id",)
