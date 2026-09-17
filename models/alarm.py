from dataclasses import dataclass


@dataclass
class Alarm:
    id: int
    time: str
    label: str
    triggered: bool = False