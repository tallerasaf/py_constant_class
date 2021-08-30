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
