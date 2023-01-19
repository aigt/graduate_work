from abc import ABC, abstractmethod
from typing import Optional, Type, TypeVar

T = TypeVar("T")  # noqa: WPS111
V = TypeVar("V")  # noqa: WPS111


class ValidatebleDescriptor(ABC):
    """Валидируемый дескриптор."""

    def __set_name__(self, owner: Type[T], name: str):
        """Назначает имя переменной дескриптора.

        Args:
            owner (Type[T]): Класс-владелец.
            name (str): Имя переменной.
        """
        self.private_name = "_{name}".format(name=name)

    def __get__(self, instance: Optional[T], objtype: Type[T] = None) -> V:
        """Получить значение.

        Args:
            instance (Optional[T]): Инстанс класса.
            objtype (Type[T], optional): Тип класса-владельца. Defaults to None.

        Returns:
            V: Значение.
        """
        return getattr(instance, self.private_name)  # type: ignore

    def __set__(self, instance: Optional[T], new_value: V) -> None:
        """Задать значение.

        Args:
            instance (Optional[T]): Инстанс класса.
            new_value (V): Значение.
        """
        self.validate(new_value)
        setattr(instance, self.private_name, new_value)

    @abstractmethod
    def validate(self, value_to_validate: V) -> None:
        """Абстрактный метод валидации.

        Args:
            value_to_validate (V): Значение.
        """
