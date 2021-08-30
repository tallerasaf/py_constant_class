from typing import Any, Callable


# noinspection PyPep8Naming
# noinspection SpellCheckingInspection
class classproperty(object):
    """
    Class property decorator.
    Example usage:
    class MyClass(object):
      @classproperty
      def value(cls):
        return '123'
    > print MyClass.value
    123
    """

    def __init__(self, func: Callable) -> None:
        self._func = func

    def __get__(self, owner_self: object, owner_cls: object) -> Any:
        return self._func(owner_cls)
