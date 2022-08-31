def handle_value_error(*, value_to_check, test_fn, message):
    red = "\033[1;31m"

    try:
        return test_fn(value_to_check)
    except ValueError:
        print(f"{red}{message}")
        exit()
