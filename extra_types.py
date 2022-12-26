class IP4:
    def __init__(self, int1: int, int2: int, int3: int, int4: int):
        byte_list: list[int] = [int1, int2, int3, int4]
        error: bool = False

        for byte in byte_list:
            if byte < 0 or byte > 255:
                error = True

        if error is True:
            raise

        else:
            self.byte4 = int4
            self.byte3 = int3
            self.byte2 = int2
            self.byte1 = int1

    @classmethod
    def with_string(cls, bytes_string: str):
        bytes_list: list[int] = []
        bytes_string = bytes_string.split(".")
        for byte in bytes_string:
            bytes_list.append(int(byte))

        byte1 = bytes_list[0]
        byte2 = bytes_list[1]
        byte3 = bytes_list[2]
        byte4 = bytes_list[3]
        return cls(byte1, byte2, byte3, byte4)

    @classmethod
    def with_tuple(cls, tuple_int: tuple[int]):
        byte1 = tuple_int[0]
        byte2 = tuple_int[1]
        byte3 = tuple_int[2]
        byte4 = tuple_int[3]
        return cls(byte1, byte2, byte3, byte4)

    def __str__(self):
        return f"{str(self.byte1)}.{str(self.byte2)}.{str(self.byte3)}.{str(self.byte4)}"


class IP6(IP4):
    pass
