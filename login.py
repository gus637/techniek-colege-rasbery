#!/usr/bin/python
def main():
    from os import system
    from inlog_data import ip_stw, user_stw
    from Computer_class import Computer

    pi: list[str] = ["DNS", "Database", "NTP", "HTTP", "Mailserver", "Gameserver", "Storage", "IRC"]
    Computer.generator(pi,user_stw,ip_stw,"RaspberryPi")

    system("clear")
    Computer.login_menu()
    system("clear")


if __name__ == "__main__":
    main()
# made by Gustave
