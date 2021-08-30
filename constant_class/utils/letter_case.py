import re
from functools import partial
from typing import Callable, Final


class LetterCaseRegex:
    CONSTANT: Final[str] = '(([A-Z_][A-Z0-9_]*)|(__.*__))$'
    SNAKE: Final[str] = '(([a-z_][a-z0-9_]*)|(__.*__))$'
    PASCAL: Final[str] = '^[A-Z][a-z]+(?:[A-Z][a-z]+)*$'
    CAMEL: Final[str] = '^[a-z]+(?:[A-Z][a-z]+)*$'


def is_text_match(text: str, regex: str) -> bool:
    return bool(re.fullmatch(regex, text))


def text_match(regex: str) -> Callable[[str], bool]:
    return partial(is_text_match, regex=regex)


class LetterCaseMatch:
    CONSTANT: Final[Callable[[str], bool]] = text_match(regex=LetterCaseRegex.CONSTANT)
    SNAKE: Final[Callable[[str], bool]] = text_match(regex=LetterCaseRegex.SNAKE)
    PASCAL: Final[Callable[[str], bool]] = text_match(regex=LetterCaseRegex.PASCAL)
    CAMEL: Final[Callable[[str], bool]] = text_match(regex=LetterCaseRegex.CAMEL)
    MIXED: Final[Callable[[str], bool]] = lambda text: True


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
