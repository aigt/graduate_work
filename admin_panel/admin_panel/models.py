from django.db import models


class Payments(models.Model):
    """Класс для отображения платежей."""

    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    external_id = models.TextField()
    external_payment = models.JSONField()
    refunded = models.BooleanField()
    system_id = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "payments"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"


class Subscribers(models.Model):
    """Класс для отображения подписок."""

    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField()
    subscriber_status = models.BooleanField()
    date_subscribe = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "subscribers"
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
