import os


class Apt:
    """
    Usage:
    You can execute simple apt commands declaratively to manage your system

    Methods:
        .change(packages)  # Changes the state of a package. packages(str) is a string to pass
                           the packages to change state
        .execute()         # Executes a command

    Example of .change() usage:
        apt_in = Apt("in", assume_yes=False)
        apt_rm = Apt("rm", assume_yes=True)

        apt_in.change("gimp")
        apt_rm.change("gimp")
    """
    command = "/bin/apt"
    no_confirm_flag = " -y "

    def __init__(self, option, assume_yes):
        possible_options = {
            "in": "install",
            "rm": "remove",
            "li": "list",
            "rup": "update",
            "up": "upgrade",
            "dup": "full-upgrade"
        }
        for i in possible_options.keys():

            if i == option:
                self.option = possible_options[i]

        self.command = f"{self.command}{self.no_confirm_flag if assume_yes else " "}{self.option}"

    def exec(self):
        if os.getuid() != 0:
            print(f"To execute {self.command} superuser permissions are needed...")
            exit(1)
        os.system(self.command)

    def change(self, packages):
        if os.getuid() != 0:
            print(f'To change state of packages superuser permissions are needed...')
            exit(1)
        os.system(f"{self.command} {packages}")
