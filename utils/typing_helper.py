import typing


class TypingHelper(object):

    @staticmethod
    def get_1_param_function_type_hints(func: typing.Callable) -> typing.Tuple[dict[str, any], any]:
        hints: dict[str, any] = typing.get_type_hints(func)
        return_type = hints.pop("return")
        param_type = list(hints.values())[0]
        return (param_type, return_type)
