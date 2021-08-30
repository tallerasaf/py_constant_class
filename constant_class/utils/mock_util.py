import inspect
from typing import List

from .list_util import flatten_list_of_lists

MOCK_FILE_NAME = 'mock.py'
MOCK_FRAME_COUNT = 2


def is_mock_the_caller(class_file_name: str) -> bool:
    try:
        return MOCK_FILE_NAME in get_caller_file_name(class_file_name)
    except IndexError:
        return False


def get_caller_file_name(class_file_name: str) -> str:
    # noinspection PyTypeChecker
    frames = [frame for frame in flatten_list_of_lists(inspect.stack()) if isinstance(frame, str)]
    frame_index = get_index_of_sub_string_in_list(frames, class_file_name)
    return frames[frame_index + MOCK_FRAME_COUNT]


def get_index_of_sub_string_in_list(lst: List, sub_string: str) -> int:
    for i, v in enumerate(lst):
        if sub_string in v:
            return i
    return -1
