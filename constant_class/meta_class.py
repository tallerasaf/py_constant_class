from typing import Any, Dict, Iterator, NoReturn, Tuple, final

from .utils.meta_helper import get_constant_members, should_allow_attribute_reassign
from .utils.sub_classes import get_base_class_names

CONSTANT_CLS_BASES_COUNT = 3


@final
class MetaConstant(type):
    __constants__: Dict[str, Any]

    def __init_subclass__(mcs, *args: object, **kwargs: object) -> object:
        raise TypeError(f'Cannot subclass from MetaClass "{mcs.__name__}".')

    def __new__(mcs, cls_name: str, bases: Tuple, cls_dict: Dict[str, Any]) -> object:
        cls_object = super().__new__(mcs, cls_name, bases, cls_dict)
        cls_bases = get_base_class_names(cls_object)
        if len(cls_bases) <= CONSTANT_CLS_BASES_COUNT:
            return cls_object
        constants = get_constant_members(cls_name, cls_dict, cls_object)
        assert constants, f'Constant class "{cls_name}" has no members.'
        cls_dict['__constants__']: Dict[str, Any] = constants
        cls_object = super().__new__(mcs, cls_name, bases, cls_dict)
        return cls_object

    def __delattr__(self, member_name: str) -> NoReturn:
        """Block attempts to delete attribute."""
        cur_obj = self.__dict__.get(member_name)
        raise AttributeError(f'Cannot delete constant, <{member_name}.{cur_obj}>.')

    def __setattr__(self, member_name: str, member_value: object) -> NoReturn:
        """Block attempts to reassign attribute."""
        cur_obj = self.__dict__.get(member_name)
        if should_allow_attribute_reassign(__file__, cur_obj, member_value):
            super().__setattr__(member_name, member_value)
        else:
            raise AttributeError(
                f'Cannot rebind constant, from <{member_name}.{cur_obj}> to <{member_name}.{member_value}>.')

    def __len__(self) -> int:
        return len(self.__constants__)

    def __iter__(self) -> Iterator:
        return iter(self.__constants__)

    def __contains__(self, item: str) -> bool:
        return item in self.__constants__ or item in self.__constants__.values()

    def __getitem__(self, key: str) -> object:
        return self.__constants__.get(key)

    def __repr__(self) -> str:
        return self.str()

    def __str__(self) -> str:
        return self.str()

    def str(self) -> str:
        return '{}({})'.format(self.__name__,
                               ', '.join(f'{key}={value}' for key, value in self.__constants__.items()))
