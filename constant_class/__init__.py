from typing import Callable, Final, Type

from .base_class import BaseConstant
from .utils.letter_case import LetterCaseMatch

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


"""
--> Python Cases
screaming_snake_case -> LONG_FUNCTION_NAME -> for Constants.
snake_case -> long_function_name -> Variable, Function, Method, Module, Package names.
pascal_case -> LongFunctionName -> Class names.
camel_case -> longFunctionName.
all_upper_case -> LONGFUNCTIONNAME.
all_lower_case -> longfunctionname.
kebab_case -> long-function-name.
screaming_kebab_case -> LONG-FUNCTION-NAME.
dot_case -> long.function.name.
screaming_dot_case -> LONG.FUNCTION.NAME.
mixed_case -> LonG.FUNC_TIO-N.NAmE.

https://plugins.jetbrains.com/plugin/2162-string-manipulation
https://realpython.com/python-pep8/#naming-styles
https://www.python.org/dev/peps/pep-0008/#id36
"""
