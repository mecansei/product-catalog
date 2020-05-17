from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Product:
    photos: List[str]
    value: float
    size: float
    brand: str = ""
    description: str = ""
    name: str = ""
    color: str = ""
