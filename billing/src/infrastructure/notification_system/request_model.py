import enum
from typing import Any, Dict, Optional

from pydantic import BaseModel


class NotificationUrgency(str, enum.Enum):
    """Типы срочности уведомления."""

    immediate = "immediate"
    usual = "usual"


class NotificationScale(str, enum.Enum):
    """Типы массовости уведомления."""

    bulk = "bulk"
    individual = "individual"


class NotificationType(str, enum.Enum):
    """Типы уведомлений."""

    show_subs = "show_subs"
    info = "info"
    welcome = "welcome"


class Meta(BaseModel):
    """Модель мета данных для модели Notification."""

    urgency: NotificationUrgency
    scale: NotificationScale
    periodic: bool


class Notification(BaseModel):
    """Модель уведомления для добавления в очередь."""

    meta: Meta
    type: NotificationType
    custom_template: Optional[Any]
    fields: Dict[str, str]
