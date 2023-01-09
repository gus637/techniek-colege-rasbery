from extra_types import IPv4
from mojule import menu
from weakref import ref


class Computer:
	instances = {}

	def __init__(self, pc_name: str, user: str | list[str], ip: IPv4 | str | tuple | None, os: str | None, strong_ref=False) -> None:
		"""

		:param pc_name: the name that the pc has.
		:param user: the user(s) that use the pc. if there are multiple users put them in a list.
		:param ip: the ip that has deen given to the pc. if the pc has no static ip, put None in this area
		:param os: the operating system that is installed onto the computer
		"""
		self.pc_name = pc_name
		self.user = user
		if type(ip) is IPv4: pass

		elif type(ip) is str: ip = IPv4.with_string(ip)

		elif type(ip) is tuple: ip = IPv4(ip)

		elif ip is None: ip = None

		else:raise TypeError

		self.ip: IPv4 | None = ip

		self.os = os

		if strong_ref: Computer.instances[pc_name] = self
		else: Computer.instances[pc_name] = ref(self)

	@staticmethod
	def generator(name_list: list[str], user_dict: dict[str, str], ip_dick: dict[str,IPv4], os) -> None:
		for name in name_list:
			Computer(name, user_dict[name], ip_dick[name], os, strong_ref=True)

	def description(self) -> None:
		if self.os is not None:
			msg2 = f"the os that is installed on the system is {self.os}"
		else:msg2 = ""

		if self.ip is not None:
			msg1 = f" and has the ip: {self.ip}"
		else:msg1 = ""

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

	def login(self) -> None:
		if self.ip is None: raise
		else:
			from os import system
			if type(self.user) is list and len(self.user) > 1:
				user: str = str(menu(self.user, "as witch user do you want to log in", type, "str"))
			else:
				user: str = self.user
			system(f"ssh {user}@{self.ip()}")

	@classmethod
	def keys(cls) -> list[str]:
		keys: list[str] = []
		for key in cls.instances.keys(): keys.append(key)
		return keys

	@classmethod
	def login_menu(cls) -> None:
		pc:cls = cls.instances[menu(cls.keys(),"where do you want to login",return_type=str)]
		pc.login()


