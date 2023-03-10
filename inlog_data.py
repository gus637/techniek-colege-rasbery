# login data from de structure wed.
# ===============================================#
from extra_types import IPv4

ip_stw: dict[str, IPv4.with_string] = {
    "DNS":			 "192.168.1.60",
    "Database":		 "192.168.1.65",
    "NTP":			 "192.168.1.55",
    "HTTP":			 "192.168.1.70",
    "Mailserver":	 "192.168.1.75",
    "Gameserver":	 "192.168.1.100",
    "Storage":		 "192.168.1.80",
    "IRC":			 "192.168.1.90",
}
user_stw: dict[str, str] = {
    "DNS":			 "user1",
    "Database":		 "user2",
    "NTP":			 "user",
    "HTTP":			 "user5",
    "Mailserver":	 "user3",
    "Gameserver":	 "user6",
    "Storage":		 "user4",
    "IRC":			 "user7",
}
password_stw: str = "12345Ab"
# ================================================#
