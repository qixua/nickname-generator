from string import ascii_lowercase as lowercase_letters
from random import choice


def nickname_generator():
    length = input("length :: ")

    try:
        length = int(length)
    except ValueError:
        print(f"The length you gave ('{length}') is not an integer.")
        exit()

    nickname_start = input("nickname start :: ")
    iter_count = input(
        "number of nicknames for the program to output :: ")

    try:
        iter_count = int(iter_count)
    except ValueError:
        print(
            f"The iteration count you gave ('{iter_count}') is not an integer.")
        exit()

    i = 0

    while i < iter_count:
        output = ""
        i += 1

        while not len(output) == length:
            rand_char = choice(list(lowercase_letters))
            output += rand_char

        if nickname_start:
            output = nickname_start + output[len(nickname_start):]

        print(
            f"""
            nickname {i}
            {"-" * length}
            {output}
            {"-" * length}"""
        )


if __name__ == "__main__":
    nickname_generator()
