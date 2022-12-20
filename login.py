#!/usr/bin/python
def main():
	from os import system
	from mojule import menu
	from inlog_data import ip_stw,user_stw

	pi=["DNS","Database","NTP","HTTP","Mailserver","Gameserver","Storage","IRC"]

	pi=menu(pi,"where do you want to log in?","str")

	system("clear")
	system("ssh "+d.user_stw[pi]+"@"+d.ip_stw[pi])

	system("clear")

if __name__=="__main__":
	main()
#made by Gustave
