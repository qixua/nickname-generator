from string import ascii_lowercase as lowercase_letters
from random import choice
from classes.ParamManager import ParamManager


def nickname_generator():
    length, nickname_start, nickname_end, iter_count, file_name = ParamManager().get_params()

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
            # created a variable instead of writing it
            # directly because of readability concerns
            diff_end = len(output) - len(nickname_end)
            output = output[0:diff_end] + nickname_end

        # keeping track of the nicknames because
        # it will be handy when printing the
        # result into a new file
        nicknames.append(output)

        if not file_name:
            print(
                f"{i}::{output}"
            )

    if file_name:
        with open(file_name, "w") as file:
            for i, n in enumerate(nicknames):
                file.write(f"{i + 1}::{n}\n")

            # there are 2 inline if's to improve readability of the messages
            # n = 1, successfully wrote a nickname to file_name
            # n > 1, successfully wrote n nicknames to file_name
            print(
                f"successfully wrote {'a' if len(nicknames) == 1 else len(nicknames)} nickname{'s' if len(nicknames) > 1 else ''} to '{file_name}'"
            )


if __name__ == "__main__":
    nickname_generator()
