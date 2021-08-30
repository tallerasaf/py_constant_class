from typing import Any, List, Set


def is_in_class_bases(cls_object: object, cls_name: str) -> bool:
    return cls_name in get_base_class_names(cls_object)


# noinspection PyUnresolvedReferences
def get_base_class_names(cls_object: object) -> List[str]:
    return [cls.__name__ for cls in cls_object.mro()]


def get_all_subclasses(python_class: object) -> Set[Any]:
    """
    Helper function to get all the subclasses of a class.
    :param python_class: Any Python class that implements __subclasses__()
    """
    # noinspection PyUnresolvedReferences
    python_class.__subclasses__()

    subclasses = set()
    check_these = [python_class]

    while check_these:
        parent = check_these.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                check_these.append(child)

    return set(sorted(subclasses, key=lambda x: x.__name__))
