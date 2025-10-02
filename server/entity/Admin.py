from dataclasses import dataclass

@dataclass
class Admin:
  id: str
  username: str
  password: str
  fullname: str
  role: str
  # note: str
  