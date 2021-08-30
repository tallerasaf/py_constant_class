# **_py_constant_class_**! 🔥

## **py_constant_class is a new Magic way to use constants with classes!**

### Features:

    1. Block attempts to delete constant members from the Class.
    2. Block attempts to reassign\rebind a constant member from the Class.
    3. Validate letter case of constant member name from the Class.
    4. Validate constant member origin type annotation is Final.
    5. Validate constant member value type is immutable built-in type.
    6. Validate constant member value type is a specific type.

### Abilities:

```
from constant_class import StrConstant

class MyConstant(StrConstant):
    FOO = 'foo1'
    BAR = 'bar1'
```

- ##### Magic Methods:
    - \__len__ -> `len(MyConstant) == 2`
    - \__iter__ -> `[c for c in MyConstant] == ['FOO', 'BAR]`
    - \__contains__ -> `'FOO' in MyConstant is True`
    - \__getitem__ -> `MyConstant['FOO'] == 'foo1'`
    - \__repr__, \__str__ -> `str(MyConstant) == 'MyConstant(FOO=foo1, BAR=bar1)'`
- ##### Regular Methods:
    - has_value(value: object) -> bool -> `MyConstant.has_value('foo1') is True`
    - has_key(key: str) -> bool -> `MyConstant.has_key('FOO') is True`
    - get(key: str, default: Optional[object] = None) -> object -> `MyConstant.get('FOO') == 'foo1'`
    - to_dict -> Dict[str, object] -> `MyConstant.to_dict == {'FOO': 'foo1', 'BAR': 'bar1}`
    - items -> List[Tuple[str, Any]] -> `MyConstant.items == [('FOO', 'foo1') ('BAR', 'bar1)]`
    - keys -> List[str] -> `MyConstant.keys == ['FOO', 'BAR']`
    - values -> List[object] -> `MyConstant.values ==  ['foo1', 'bar1']`
- ##### Special Attributes:
    - \__letter_case_match_func__: Callable[[str], bool] ->  Member name must be specific letter case.
    - \__error_msg__: str ->  Error when Member name is not a specific letter case.
    - \__strict_type__: Type = object -> Default - Member value type must be specific type.
    - \__strict_final__: bool = True -> Default - Member origin type annotation must be <_Final_>.
    - \__strict_immutable__: bool = True -> Default - Member value type must be <_immutable_> built-in type.

### Constant Classes:

- **_Constant_**:
    - Member name must be <_SCREAMING_SNAKE_CASE_>.
    - Member origin type annotation must be <_Final_>.
    - Member value type must be <_immutable_> built-in type.
- **_StrConstant_**:
    - Member name must be <_SCREAMING_SNAKE_CASE_>.
    - Member origin type annotation must be <_Final_>.
    - Member value type must be <_str_> type.
- **_IntConstant_**:
    - Member name must be <_SCREAMING_SNAKE_CASE_>.
    - Member origin type annotation must be <_Final_>.
    - Member value type must be <_int_> type.
- **_SnakeConstant_**:
    - Member name must be <_snake_case_>.
    - Member origin type annotation must be <_Final_>.
    - Member value type must be <_immutable_> built-in type.
- **_PascalConstant_**:
    - Member name must be <_PascalCase_>.
    - Member origin type annotation must be <_Final_>.
    - Member value type must be <_immutable_> built-in type.
- **_CamelConstant_**:
    - Member name must be <_camelCase_>.
    - Member origin type annotation must be <_Final_>.
    - Member value type must be <_immutable_> built-in type.
- **_MixedConstant_**:
    - Anything allowed.

###### ![Const Image](https://www.fluentcpp.com/wp-content/uploads/2018/05/cont_ref_not_const.png)

## Author:

- [Asaf Taller](https://github.com/tallerasaf)

##### Copyright (C) [2021] [tallerasaf].
