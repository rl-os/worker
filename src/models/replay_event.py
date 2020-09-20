from src.utils import nested_dataclass


@nested_dataclass
class ReplayEvent(object):
    time_since_previous_action: int
    x: float
    y: float
    keys_pressed: int
