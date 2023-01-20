from abc import ABC, abstractmethod
from typing import Optional, Type, TypeVar

T = TypeVar("T")  # noqa: WPS111
V = TypeVar("V")  # noqa: WPS111


class ValidatebleDescriptor(ABC):
    """Валидируемый дескриптор."""

    def __set_name__(self, owner: Type[T], name: str) -> None:
        """Назначает имя переменной дескриптора.

        Args:
            owner (Type[T]): Класс-владелец.
            name (str): Имя переменной.

        Raises:
            SyntaxError: Если в классе нет аннотации типа.
        """
        self.private_name = "_{name}".format(name=name)
        self.value_type = owner.__annotations__.get(name)
        if self.value_type is None:
            raise SyntaxError(
                "{class_name}.{field_name} must have a type annotation.".format(
                    class_name=owner.__name__,
                    field_name=name,
                ),
            )

    def __get__(
        self,
        instance: Optional[T],
        objtype: Optional[Type[T]] = None,
    ) -> V:  # type: ignore
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

        Raises:
            TypeError: Если у переменной неверный тип.
        """
        # Проверка типа значения на соответствие аннотации в классе
        if not isinstance(new_value, self.value_type):  # type: ignore
            raise TypeError(
                "Wrong type {value_type} of value {new_value}, must be {expected_value_type}".format(
                    value_type=type(new_value),
                    new_value=new_value,
                    expected_value_type=self.value_type,
                ),
            )

        # Валидация значения
        self.validate(new_value)

        # Присвоение значения
        setattr(instance, self.private_name, new_value)

    @abstractmethod
    def validate(self, value_to_validate: V) -> None:
        """Абстрактный метод валидации.

        Args:
            value_to_validate (V): Значение.
        """


class ReadOnlyValidatebleDescriptor(ValidatebleDescriptor):
    """Валидируемый дескриптор только для чтение."""

    def __set__(self, instance: Optional[T], new_value: V) -> None:
        """Задать значение.

        Args:
            instance (Optional[T]): Инстанс класса.
            new_value (V): Значение.

        Raises:
            AttributeError: При попытке присвоения значения полю.
        """
        # Разрешить присваивать только начальное значение
        if hasattr(instance, self.private_name):  # noqa: WPS421
            raise AttributeError(
                "Field {class_name}.{field_name} is not availiable to set.".format(
                    class_name=type(instance).__name__,
                    field_name=self.private_name,
                ),
            )

        super().__set__(instance, new_value)
