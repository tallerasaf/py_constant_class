from typing import Any, List


def flatten_list_of_lists(list_of_list: List[List[Any]]) -> List[Any]:
    return [var for sublist in list_of_list for var in sublist or []]


def remove_duplicates_from_list(my_list: List[Any]) -> List[Any]:
    return list({}.fromkeys(my_list))


def remove_none_values_from_list(my_list: List[Any]) -> List[Any]:
    return list(filter(None, my_list))
