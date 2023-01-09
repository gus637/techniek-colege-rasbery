class IPv4:
	def __init__(self, *ints: int | tuple[int,int,int,int]):

		if type(ints[0]) == tuple: ints = ints[0]

		for byte in ints:
			if byte < 0 or byte > 255: raise

		else:
			self.byte1, self.byte2, self.byte3, self.byte4 = ints

	@classmethod
	def with_string(cls, bytes_string: str):
		bytes_string = bytes_string.split(".")
		new_list = []
		for str_ in  bytes_string:
			new_list.append(int(str_))
		int1, int2, int3, int4 = new_list

		return cls(int1,int2,int3,int4)

	def __str__(self):
		return f"{str(self.byte1)}.{str(self.byte2)}.{str(self.byte3)}.{str(self.byte4)}"

	def __call__(self):
		return str(self)

	def ping(self):
		from os import system; system(f"ping {self()}")

	@staticmethod
	def ip_chaker(ip:tuple[int,int,int,int]):
		for i in ip:
			if i < 0 or i > 255: raise BytesWarning(
				"one byte ore more were not within 0-255, pls make sure that all 4 sections of the address fit in a byte")

	@property
	def ip(self):
		return str(self)
