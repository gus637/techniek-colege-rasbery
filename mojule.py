if __name__ == "__main__":
    from os import system

from extra_types import IP4, IP6


def modes(pos_mode: list[str] | tuple[str], mode: list[str] | tuple[str]) -> str:
    """

    :param pos_mode: the mods that can de
    :param mode: the mods can bi
    :return: a string of ones and/or zeros
    """
    # print(mode)
    code: str = str()
    for item in pos_mode:
        if item in mode:
            code = code + "1"
        else:
            code = code + "0"
    return code


def input_num(minimum: int, maximum: int, *default_num: int) -> int | None:
    """
    :param minimum: the minimum number that you want the user tho choose
    :param maximum: the biggest number you want the user to choose
    :param default_num:
    :return: the int that is returned by the user is given to the program
    """
    try:
        num: int = int(input())

    except TypeError:
        print("pleas type a number")
        num: int = input_num(minimum, maximum, default_num[0])

    except KeyboardInterrupt:
        raise
        pass

    except RecursionError:
        try:
            default_num

        except NameError:
            return

        else:
            return default_num[0]
    if num < minimum or num > maximum:
        print("not in range")
        num = input_num(minimum, maximum, default_num[0])
        return num


def menu(options: list[str] | tuple[str], msg: str, *mode: str) -> int | str:
    """
    import this to make a simpel menu for the user.

    how to use:
    
    put a LIST with options in the first slot and a msg in the second,
    then you can set the mode for the output:"int" or "str".
    mode
    "int"=makes te menu return an integer (on by default).
    "str"=make the menu return a string.

    you can also set it so that multiple choices can be made by entering "multi"

    Returns
    -------
    object
    """

    code = modes(["exit", "str", "multi", "bug"], mode)  # 0="exit" 1="str"/"int" 2="multi" 3="bug"

    true: str = "1"
    num: int = 0
    str_len: int = 0  #
    num_len: int = len(str(len(options))) - 1  #
    picked: int
    picks: list[int] = []
    if code[3] == true:
        print(code)
    if code[0] == true:
        return "exit"
    for item in options:  # iterates tru all the items in the given list of options and sets "str_len"'s integer to the len of the longest string
        if str_len < len(
                item):  # looks at "str_len" and the current item to see if the item's len is bigger then the last item's len
            str_len = len(item)  # if so sets "str_len" to the bigger number
    str_len += 2  # ads 2 to the num of "str_len"

    print("\n\n                                 {msg)".format(msg=msg))  # prints the given msg at the top of the menu
    print("                               ", "_" * (
            str_len + 7 + num_len))  # prints the top line of the menu (the line's len is dependent of the longest string
    for item in options:  # these lines of code are responsive for printing the menu and options
        num += 1  #
        p1: int = str_len - len(item)  #
        p2: str = " " * p1  #
        p3: int = len(str(num)) - 1
        print("                               |", num, " " * (num_len - p3) + "|", item, p2, "|")
    if code[2] == true:
        num += 1
        p1: int = str_len - len("finis")  #
        p2: str = " " * p1  #
        p3: int = len(str(num)) - 1
        print("                               |", num, " " * (num_len - p3) + "|", "finis", p2, "|")
    print("                               |___" + "_" * num_len + "|" + "_" * (str_len + 3) + "|")

    if code[2] == true:
        print("type the numbers of with option you want to choose")
        don = False
        while don is not True:
            picked: int = input_num(1, num, num)
            if picked is num:
                don = True
            else:
                picks.append(picked)
        if code[1] is true:
            for picked in picks:
                yield options[picked]

        else:
            return picks
    else:
        print("type the number of the option that you want to choose")
        picked = input_num(1, num)
        if code[1] == true:
            return options[picked - 1]
        else:
            return picked


class Computer:
    def __init__(self, pc_name: str, user: str | list[str], ip: IP4 | IP6 | str | tuple | None, os: str | None):
        """

        :param pc_name: the name that the pc has.
        :param user: the user(s) that use the pc. if there are multiple users put them in a list.
        :param ip: the ip that has deen given to the pc. if the pc has no static ip, put None in this area
        :param os: the operating system that is installed onto the computer
        """
        self.pc_name = pc_name
        self.user = user
        if type(ip) is IP4:
            self.ip = ip

        elif type(ip) is str:
            self.ip = IP4.with_string(ip)

        elif type(ip) is tuple:
            self.ip = IP4.with_tuple(ip)

        elif ip is None:
            self.ip = None

        else:
            raise TypeError

        self.os = os

    def description(self):
        if self.os is not None:
            msg2 = f"the os that is installed on the system is {self.os}"
        else:
            msg2 = ""

        if self.ip is not None:
            msg1 = f" and has the ip: {self.ip}"
        else:
            msg1 = " it has no ip"

        if type(self.user) is list:
            num_users: int = len(self.user)
            if num_users > 1:
                str_users: str = self.user[0]
                num_users -= 1
                i: int = 1
                while num_users > 1:
                    str_users = str_users + f", {self.user[i]}"
                    i += 1
                    num_users -= 1
                str_users = str_users + f" and {self.user[i]}"
                print(
                    f"this pc has the name: {self.pc_name}{msg1}, and it is used by: {str_users}. {msg2}")
            else:
                print(
                    f"this pc has the name {self.pc_name}{msg1}, it is used by {self.user[0]}. {msg2}")

        else:
            print(
                f"this pc has the name: {self.pc_name}{msg1}, and it is used by {self.user}. {msg2}")

    # noinspection PyTypeChecker
    def login(self):
        if self.ip is not None:
            try:
                if type(self.user) is list and len(self.user) > 1:
                    user: str = str(menu(self.user, "as witch user do you want to log in", "str"))
                else:
                    user: str = self.user
                system(f"ssh {user}@{str(self.ip)}")
            except NameError:
                print("pleas import system from os")
