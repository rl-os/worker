from pydantic import BaseModel


class ReplayEvent(BaseModel):
    time_since_previous_action: int
    x: float
    y: float
    keys_pressed: int
