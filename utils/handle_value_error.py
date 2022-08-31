from types import FunctionType


def handle_value_error(
    *,
    value_to_check,
    type_conv_fn: FunctionType,
    message: str
):
    red = "\033[1;31m"

    try:
        return type_conv_fn(value_to_check)
    except ValueError:
        print(f"{red}{message}")
        exit()
