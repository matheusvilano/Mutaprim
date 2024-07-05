from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterable, Any, Type

T = TypeVar("T", bool, int, float, str, bytes)


class MutablePrimitive(ABC, Generic[T]):

    def __init__(self, value: T = None):
        """
        Constructor for mutable primitives.
        :param value: The value to initialize the object to. If None, a default will be used.
        """
        super().__init__()
        self._value: T = value if value is not None else self._get_default()
        if not self._validate_type(self._value):
            raise TypeError("The provided value is of the wrong type.")

    @staticmethod
    @abstractmethod
    def _validate_type(value: Any) -> bool:
        """
        Type validator.
        :param value: The value to validate the type of.
        :return: `True` if the type matches the expected type (e.g. `bool` for `MutableBool`); else, `False`.
        """
        pass

    @staticmethod
    @abstractmethod
    def _get_default() -> T:
        """
        Default getter.
        :return: The default value of the underlying type (`False` for `MutableBool`).
        """
        pass

    @staticmethod
    @abstractmethod
    def _get_type() -> type:
        """
        Type getter.
        :return: The underlying type. In other words, the type of the `value`.
        """
        pass

    def get(self) -> T:
        """
        Getter. Same as getting via the property `value`.
        :return: The current value.
        """
        return self._value

    def set(self, value):
        """
        Setter. Same as setting via the property `value`.
        :param value: The new value.
        """
        self._value = value

    @property
    def value(self) -> T:
        """
        Getter. Same as `get`.
        :return: The current value.
        """
        return self.get()

    @value.setter
    def value(self, value):
        """
        Setter. Same as `set`.
        :param value: The new value.
        """
        self.set(value)

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value

    def __abs__(self):
        return self._value.__abs__()

    def __add__(self, other):
        return self._value.__add__(other)

    def __and__(self, other):
        return self._value.__and__(other)

    def __bool__(self):
        return self._value.__bool__()

    def __contains__(self, item):
        return self._value.__contains__(item)

    def __dir__(self) -> Iterable[str]:
        return self._value.__dir__()

    def __divmod__(self, other):
        return self._value.__divmod__(other)

    def __eq__(self, other):
        return self._value.__eq__(other)

    def __float__(self):
        return self._value.__float__()

    def __floor__(self):
        return self._value.__floor__()

    def __floordiv__(self, other):
        return self._value.__floordiv__(other)

    def __format__(self, format_spec):
        return self._value.__format__(format_spec)

    def __ge__(self, other):
        return self._value.__ge__(other)

    def __gt__(self, other):
        return self._value.__gt__(other)

    def __hash__(self):
        return self._value.__hash__()

    def __index__(self):
        return self._value.__index__()

    def __instancecheck__(self, instance):
        return isinstance(instance, self._value.__class__)

    def __int__(self):
        return self._value.__int__()

    def __invert__(self):
        return self._value.__invert__()

    def __iter__(self):
        return self._value.__iter__()

    def __le__(self, other):
        return self._value.__le__(other)

    def __len__(self):
        return self._value.__len__()

    def __lshift__(self, other):
        return self._value.__lshift__(other)

    def __lt__(self, other):
        return self._value.__lt__(other)

    def __mod__(self, other):
        return self._value.__mod__(other)

    def __mul__(self, other):
        return self._value.__mul__(other)

    def __ne__(self, other):
        return self._value.__ne__(other)

    def __neg__(self):
        return self._value.__neg__()

    def __or__(self, other):
        return self._value.__or__(other)

    def __pos__(self):
        return self._value.__pos__()

    def __pow__(self, power, modulo=None):
        return self._value.__pow__(power, modulo)

    def __radd__(self, other):
        return self._value.__radd__(other)

    def __rand__(self, other):
        return self._value.__rand__(other)

    def __rdivmod__(self, other):
        return self._value.__rdivmod__(other)

    def __reduce__(self):
        return self._value.__reduce__()

    def __reduce_ex__(self, protocol):
        return self._value.__reduce_ex__(protocol)

    def __repr__(self):
        return self._value.__repr__()

    def __reversed__(self):
        return self._value.__reversed__()

    def __rfloordiv__(self, other):
        return self._value.__rfloordiv__(other)

    def __rlshift__(self, other):
        return self._value.__rlshift__(other)

    def __rmod__(self, other):
        return self._value.__rmod__(other)

    def __rmul__(self, other):
        return self._value.__rmul__(other)

    def __ror__(self, other):
        return self._value.__ror__(other)

    def __round__(self, n=None):
        return self._value.__round__(n)

    def __rpow__(self, other):
        return self._value.__rpow__(other)

    def __rrshift__(self, other):
        return self._value.__rrshift__(other)

    def __rshift__(self, other):
        return self._value.__rshift__(other)

    def __rsub__(self, other):
        return self._value.__rsub__(other)

    def __rtruediv__(self, other):
        return self._value.__rtruediv__(other)

    def __rxor__(self, other):
        return self._value.__rxor__(other)

    def __sizeof__(self):
        return self._value.__sizeof__()

    def __str__(self):
        return self._value.__str__()

    def __sub__(self, other):
        return self._value.__sub__(other)

    def __subclasscheck__(self, subclass):
        issubclass(self._value.__class__, subclass)

    def __truediv__(self, other):
        return self._value.__truediv__(other)

    def __xor__(self, other):
        return self._value.__xor__(other)


class MutableBool(MutablePrimitive[bool]):

    @staticmethod
    def _validate_type(value: Any) -> bool:
        return isinstance(value, bool)

    @staticmethod
    def _get_default() -> bool:
        return bool()

    @staticmethod
    def _get_type() -> Type[bool]:
        return bool


class MutableInt(MutablePrimitive[int]):

    @staticmethod
    def _validate_type(value: Any) -> bool:
        return isinstance(value, int)

    @staticmethod
    def _get_default() -> int:
        return int()

    @staticmethod
    def _get_type() -> Type[int]:
        return int


class MutableFloat(MutablePrimitive[float]):

    @staticmethod
    def _validate_type(value: Any) -> bool:
        return isinstance(value, float)

    @staticmethod
    def _get_default() -> float:
        return float()

    @staticmethod
    def _get_type() -> Type[float]:
        return float


class MutableStr(MutablePrimitive[str]):

    @staticmethod
    def _validate_type(value: Any) -> bool:
        return isinstance(value, str)

    @staticmethod
    def _get_default() -> str:
        return str()

    @staticmethod
    def _get_type() -> Type[str]:
        return str


class MutableBytes(MutablePrimitive[bytes]):

    @staticmethod
    def _validate_type(value: Any) -> bool:
        return isinstance(value, bytes)

    @staticmethod
    def _get_default() -> bytes:
        return bytes()

    @staticmethod
    def _get_type() -> Type[bytes]:
        return bytes
