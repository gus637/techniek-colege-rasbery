
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


def menu(options: list[str] | tuple[str], msg: str, return_type=int, multy=False) -> int | str | list[int | str]:
    """
    import this to make a simpel menu for the user.

    how to use:
    
    put a LIST with options in the first slot and a msg in the second,
    then you can set the mode for the output:"int" or "str".
    mode
    "int"=makes te menu return an integer (on by default).
    "str"=make the menu return a string.

    you can also set it so that multiple choices can be made by entering "multi"

    Parameters
    ----------
    options
    msg
    return_type
    multy

    Returns
    -------
    int or str or list
    """
    num: int = 0
    str_len: int = 0  #
    num_len: int = len(str(len(options))) - 1  #
    picked: int
    picks: list[int] = []

    for item in options:  # iterates tru all the items in the given list of options and sets "str_len"'s integer to the len of the longest string
        if str_len < len(
                item):  # looks at "str_len" and the current item to see if the item's len is bigger then the last item's len
            str_len = len(item)  # if so sets "str_len" to the bigger number
    str_len += 2  # ads 2 to the num of "str_len"

    print(f"\n\n                                 {msg})")  # prints the given msg at the top of the menu
    print("                               ", "_" * (str_len + 7 + num_len))  # prints the top line of the menu (the line's len is dependent of the longest string
    for item in options:  # these lines of code are responsive for printing the menu and options
        num += 1  #
        p1: int = str_len - len(item)  #
        p3: int = len(str(num)) - 1
        print(f"                               | {num} { ' ' * (num_len - p3)}| {item} {' ' * p1} |")
    if multy:
        num += 1
        p1: int = str_len - len("finis")  #
        p2: str = " " * p1  #
        p3: int = len(str(num)) - 1
        print("                               |", num, " " * (num_len - p3) + "|", "finis", p2, "|")
    print("                               |___" + "_" * num_len + "|" + "_" * (str_len + 3) + "|")

    if multy:
        print("type the numbers of with options you want to choose")
        while True:
            picked: int = input_num(1, num, num)
            if picked is num:break
            elif picked in picks: picks.remove(picked)
            else:picks.append(picked)
            print("selected:", picks)
        if return_type is str:
            list_str = []
            for picked in picks:
                list_str.append(options[picked])
            return list_str

        elif return_type is int:return picks
    else:
        print("type the number of the option that you want to choose")
        picked = input_num(1, num)
        if return_type is str:return options[picked - 1]
        elif return_type is int:return picked


