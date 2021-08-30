from typing import Any, Callable, Dict, List, Optional, Tuple, Type, final

from constant_class.meta_class import MetaConstant


class BaseConstant(metaclass=MetaConstant):
    """Base class for constant namespaces."""
    __slots__ = ()

    __constants__: Dict[str, Any] = {}
    __letter_case_match_func__: Callable[[str], bool]
    __error_msg__: str
    __strict_type__: Type = object
    __strict_final__: bool = True

    @classmethod
    @final
    def has_value(cls, value: object) -> bool:
        return value in list(cls.values())

    @classmethod
    @final
    def has_key(cls, key: str) -> bool:
        return key in cls

    @classmethod
    @final
    def get(cls, key: str, default: Optional[object] = None) -> object:
        try:
            return cls[key]
        except KeyError:
            return default

    @classmethod
    @final
    def to_dict(cls) -> Dict[str, object]:
        return cls.__constants__

    @classmethod
    @final
    def items(cls) -> List[Tuple[str, Any]]:
        # noinspection PyTypeChecker
        return list(cls.__constants__.items())

    @classmethod
    @final
    def keys(cls) -> List[str]:
        return list(cls.__constants__.keys())

    @classmethod
    @final
    def values(cls) -> List[object]:
        return list(cls.__constants__.values())
