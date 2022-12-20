#!/usr/bin/python
def main():
	from os import system
	from mojule import menu
	import inlog_data as d

	pi=["DNS","Database","NTP","HTTP","Mailserver","Gameserver","Storage","IRC"]

	pi=menu(pi,"where do you want to log in?","str")

	system("clear")
	system("ssh "+d.user_stw[pi]+"@"+d.ip_stw[pi])

	system("clear")

if __name__=="__main__":
	main()
#made by Gustave
