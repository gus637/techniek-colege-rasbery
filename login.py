#!/usr/bin/python
def main():
    from os import system
    from mojule import menu
    from inlog_data import ip_stw, user_stw

    pi: list[str] = ["DNS", "Database", "NTP", "HTTP", "Mailserver", "Gameserver", "Storage", "IRC"]

    pi: str = str(menu(pi, "where do you want to log in?", "str"))

    system("clear")
    system(f'ssh {user_stw[pi]}@{ip_stw[pi]}')
    system("clear")


if __name__ == "__main__":
    main()
# made by Gustave
