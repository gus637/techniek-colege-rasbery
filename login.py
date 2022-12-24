#!/usr/bin/python
def main():
    from os import system
    from mojule import menu
    from inlog_data import ip_stw, user_stw

    pi: list[str] = ["DNS", "Database", "NTP", "HTTP", "Mailserver", "Gameserver", "Storage", "IRC"]

    pi: str = menu(pi,"where do you want to log in?", "str")

    system("clear")
    command = "ssh {user}@{ip}".format(user=user_stw[pi], ip=ip_stw[pi])
    system(command)
    system("clear")


if __name__ == "__main__":
    main()
# made by Gustave
