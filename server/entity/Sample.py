from dataclasses import dataclass
from entity import Admin

@dataclass
class Sample:
  id: str
  user_id: str
  product_id: str
  label: int
  admin: Admin
  dataset: None
