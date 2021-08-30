from typing import Callable, Final, Type

from .base_class import BaseConstant
from .utils.letter_case import LetterCaseMatch

__doc__ = 'py_constant_class Lib! -> A new Magic way to use constants with classes.'
__author__ = 'tallerasaf'
__all__ = []


class Constant(BaseConstant):
    __letter_case_match_func__: Final[Callable[[str], bool]] = LetterCaseMatch.CONSTANT
    __error_msg__: Final[str] = 'SCREAMING_SNAKE_CASE for Constant.'


class StrConstant(BaseConstant):
    __letter_case_match_func__: Final[Callable[[str], bool]] = LetterCaseMatch.CONSTANT
    __error_msg__: Final[str] = 'SCREAMING_SNAKE_CASE for StrConstant.'
    __strict_type__: Final[Type] = str


class IntConstant(BaseConstant):
    __letter_case_match_func__: Final[Callable[[str], bool]] = LetterCaseMatch.CONSTANT
    __error_msg__: Final[str] = 'SCREAMING_SNAKE_CASE for IntConstant.'
    __strict_type__: Final[Type] = int


class SnakeConstant(BaseConstant):
    __letter_case_match_func__: Final[Callable[[str], bool]] = LetterCaseMatch.SNAKE
    __error_msg__: Final[str] = 'snake_case for SnakeConstant.'


class PascalConstant(BaseConstant):
    __letter_case_match_func__: Final[Callable[[str], bool]] = LetterCaseMatch.PASCAL
    __error_msg__: Final[str] = 'PascalCase for PascalConstant.'


class CamelConstant(BaseConstant):
    __letter_case_match_func__: Final[Callable[[str], bool]] = LetterCaseMatch.CAMEL
    __error_msg__: Final[str] = 'camelCase for CamelConstant.'


class MixedConstant(BaseConstant):
    __letter_case_match_func__: Final[Callable[[str], bool]] = LetterCaseMatch.MIXED
    __strict_final__: Final[bool] = False
    __strict_immutable__: Final[bool] = False
