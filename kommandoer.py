def command():
    return "command"


def takeoff():
    return "takeoff"


def land():
    return "land"


def move_up(distance: int):
    return f"up {distance}"


def move_down(distance: int):
    return f"down {distance}"


def move_left(distance: int):
    return f"left {distance}"


def move_right(distance: int):
    return f"right {distance}"


def move_forward(distance: int):
    return f"forward {distance}"


def move_back(distance: int):
    return f"back {distance}"


def flip(direction: str):
    return f"flip {direction}"
