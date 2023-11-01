class Error(Exception):
    pass


class FileNameError(Error):
    pass


class CommandError(Error):
    pass


def copy_file(command: str) -> None:
    first_arg, second_arg, third_arg = command.split()
    if first_arg != "cp":
        raise CommandError("You privided the wrong command")
    if second_arg == third_arg:
        raise FileNameError("File names can not be equal")
    content_to_copy = " "
    with open(second_arg, "r") as source_file, open(third_arg, "w") as destination_file:
        content_to_copy = source_file.read()
        destination_file.write(content_to_copy)
