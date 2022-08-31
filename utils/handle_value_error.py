def handle_value_error(*, value_to_check, test_fn, message):
    try:
        return test_fn(value_to_check)
    except ValueError:
        print(message)
        exit()
