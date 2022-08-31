from utils.handle_value_error import handle_value_error


class ParamManager:
    def __init__(self):
        self.length = input("length :: ")
        self.nickname_start = input("nickname start :: ")
        self.nickname_end = input("nickname end :: ")
        self.iter_count = input(
            "number of nicknames for the program to output :: ")
        self.file_name = input(
            "file name to save the nicknames in ('no' to reject) :: ")

    def get_params(self) -> tuple:
        self.length = handle_value_error(
            value_to_check=self.length,
            test_fn=int,
            message=f"The length you gave ('{self.length}') is not an integer."
        )

        self.iter_count = handle_value_error(
            value_to_check=self.iter_count,
            test_fn=int,
            message=f"The iteration count you gave ('{self.iter_count}') is not an integer."
        )

        self.file_name = False if self.file_name.lower() == "no" else self.file_name

        return self.length, self.nickname_start, self.nickname_end, self.iter_count, self.file_name
