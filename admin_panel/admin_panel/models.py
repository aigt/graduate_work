import uuid

from django.db import models

class Subscribers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    subsciber_status = models.BooleanField(default=False)
    date_subsctibe = models.DateTimeField(auto_now=True)
