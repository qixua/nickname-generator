from string import ascii_lowercase as lowercase_letters
from random import choice
from classes.ParamManager import ParamManager


def nickname_generator():
    # ====ASK AND SAVE USER-SUPPLIED PARAMETERS====
    length, nickname_start, nickname_end, iter_count, file_name = ParamManager().get_params()

    # ====GENERATE NICKNAMES ACCORDING TO GIVEN PARAMETERS====
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
