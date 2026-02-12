from dataclasses import dataclass
from datetime import datetime

@dataclass
class Price:
    value: int
    timestamp: datetime