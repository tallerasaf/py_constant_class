import inspect
from typing import Any, Dict, Final, NoReturn, get_origin, get_type_hints
from unittest.mock import MagicMock, PropertyMock

from .mock_util import is_mock_the_caller

DUNDER_SCORE = '__'


def get_constant_members(cls_name: str, cls_dict: Dict[str, Any], cls_object: object) -> Dict[str, Any]:
    return {
        member_name: member_value
        for member_name, member_value in cls_dict.items()
        if is_valid_constant_member(cls_name, cls_object, member_name, member_value)
    }


def is_valid_constant_member(cls_name: str, cls_object: object,
                             member_name: str, member_value: object) -> bool:
    if should_skip_member(member_name, member_value):
        return False
    validate_member(cls_name, cls_object, member_name, member_value)
    return True


def validate_member(cls_name: str, cls_object: object, member_name: str, member_value: object) -> NoReturn:
    # noinspection PyUnresolvedReferences
    assert cls_object.__letter_case_match_func__(member_name), \
        f'Bad constant <{cls_name}.{member_name}> name, use {cls_object.__error_msg__}.'

    # noinspection PyUnresolvedReferences
    assert isinstance(member_value, cls_object.__strict_type__), \
        f'Constant member type must be {cls_object.__strict_type__}.'

    # noinspection PyUnresolvedReferences
    if cls_object.__strict_final__:
        assert is_member_origin_type_final(cls_object, member_name), 'Constant member origin type must be Final.'


def should_skip_member(member_name: str, member_value: object) -> bool:
    return member_name.startswith(DUNDER_SCORE) or inspect.isfunction(member_value) \
           or inspect.ismethoddescriptor(member_value)


def is_member_origin_type_final(cls_object: object, member_name: str) -> bool:
    origin_type = get_type_hints(cls_object).get(member_name)
    while origin_type is not None:
        if origin_type is Final:
            return True
        origin_type = get_origin(origin_type)
    return False


def should_allow_attribute_reassign(__file__: str, cur_obj: object, member_value: object) -> bool:
    return isinstance(member_value, (MagicMock, PropertyMock)) \
           or isinstance(cur_obj, (MagicMock, PropertyMock)) \
           or is_mock_the_caller(__file__)
