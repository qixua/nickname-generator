from string import ascii_lowercase as lowercase_letters
from random import choice
from utils.handle_value_error import handle_value_error


def nickname_generator():
    length = input("length :: ")
    length = handle_value_error(value_to_check=length, test_fn=int,
                                message=f"The length you gave ('{length}') is not an integer.")

    nickname_start = input("nickname start :: ")
    iter_count = input(
        "number of nicknames for the program to output :: ")
    iter_count = handle_value_error(value_to_check=iter_count, test_fn=int,
                                    message=f"The iteration count you gave ('{iter_count}') is not an integer.")

    nickname_end = input("nickname end :: ")

    file_name = input(
        "file name to save the nicknames in ('no' to reject) :: ")
    file_name = False if file_name.lower() == "no" else file_name

    i = 0
    nicknames = []

    while i < iter_count:
        output = ""
        i += 1

        while not len(output) == length:
            rand_char = choice(list(lowercase_letters))
            output += rand_char

        if nickname_start:
            output = nickname_start + output[len(nickname_start):]

        if nickname_end:
            diff_end = len(output) - len(nickname_end)
            output = output[0:diff_end] + nickname_end

        nicknames.append(output)

        if not file_name:
            print(
                f"{i}::{output}"
            )

    if file_name:
        with open(file_name, "w") as file:
            for i, n in enumerate(nicknames):
                file.write(f"{i + 1}::{n}\n")

            print(
                f"successfully wrote {'a' if len(nicknames) == 1 else len(nicknames)} nickname{'s' if len(nicknames) > 1 else ''} to '{file_name}'")


if __name__ == "__main__":
    nickname_generator()
