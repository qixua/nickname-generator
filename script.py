from string import ascii_lowercase
from random import choice


def nickname_generator():
    length = int(input("length :: "))
    nickname_start = input("nickname start :: ")
    iteration = 0

    while iteration <= 20:
        output = ""
        iteration += 1

        for i in range(length):
            rand_char = choice(list(ascii_lowercase))
            output += rand_char

        if nickname_start:
            output = nickname_start + output[1:]

            while not len(output) == length:
                output = output[: len(output) - 1]

        print(
            f"""
            nickname {iteration - 1}
            {"-" * length}
            {output}
            {"-" * length}"""
        )


if __name__ == "__main__":
    nickname_generator()
