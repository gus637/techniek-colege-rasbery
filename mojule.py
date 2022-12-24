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


def input_num(minimum: int, maximum: int, *default_num: int) -> int:
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

    except RecursionError:
        try:
            defalt_num

        except NameError:
            return none

        else:
            return defalt_num[0]

    else:
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
    """

    code = modes(["exit", "str", "multi", "bug"], mode)  # 0="exit" 1="str"/"int" 2="multi" 3="bug"

    true: str = "1"
    num: int = 0
    str_len: int = 0  #
    num_len: int = len(str(len(options))) - 1  #
    picked: int
    picks: list[int] = []
    coiss: list[int] = []
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
    for item in options:  #
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
            picked:int = input_num(1,num, num)
            if picked is num:
                don = True
            else:
                picks = picks + picked
        if code[1] is true:
            for picked in picks:
                yield options[picked - 1]
        else:
            for picked in picks:
                yield picked
    else:
        print("type the number of the option that you want to choose")
        picked = getNumUser(1, num)
        if code[1] == true:
            return options[picked - 1]
        else:
            return picked


class Computer:
    def __init__(self, pc_name: str, user: str | list[str], ip: str, os: str):
        """

        :param pc_name: the name that the pc has.
        :param user: the user(s) that use the pc. if there are multiple users put them in a list.
        :param ip: the ip that has deen given to the pc. if the pc has a static ip, put none in this area
        :param os:
        """
        self.pc_name = pc_name
        self.user = user
        self.ip = ip
        self.os = os

    def description(self):
        if type(self.user) is list:
            num_users: int = len(self.user)
            if num_users > 1:
                str_users: str = self.user[0]
                num_users -= 1
                i: int = 1
                while num_users > 1:
                    str_users = str_users + ", {0}".format(self.user[i])
                    i += 1
                    num_users -= 1
                str_users = str_users + " and " + self.user[i]
                msg = "this pc has the name {name} and has the ip {ip}, and it is used by: {users}. the os that is installed on the system is {os}".format(name=self.pc_name, ip=self.ip, users=str_users, os=self.os)
                print(msg)
            else:
                msg = "this pc has the has the name {name} and has the ip {ip}, it is used by {user}. the os that is installed on the system is {os}".format(name=self.pc_name, ip=self.ip, user=self.user[0], os=self.os)
                print(msg)

        else:
            msg = "this pc has the has the name {name} and has the ip {ip}, and it is used by {user}. the os that is installed on the system is {os}".format(name=self.pc_name, ip=self.ip, user=self.user, os=self.os)
            print(msg)

    def login(self):
        from os import system
        if type(self.user) is list and len(self.user) > 1:
            user: str = menu(self.user, "as witch user do you want to log in", "str")
        else:
            user: str = self.user
        ssh: str = "ssh {user}@{ip}".format(user=user, ip=self.ip)
        system(ssh)


if __name__ == "__main__":
    test = Computer("dorland_leptop", ["Gustave","zet"], "192.168.1.100", "windows 10")
    test.description()
    test.login()