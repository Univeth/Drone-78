def command():
    return "command"


def takeoff():
    return "takeoff"


def land():
    return "land"


def streamon():
    return "streamon"


def streamoff():
    return "streamoff"


def emergency():
    return "emergency"


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


def clockwise(degrees: int):
    return f"cw {degrees}"


def counterclockwise(degrees: int):
    return f"ccw {degrees}"


def flip(direction: str):
    return f"flip {direction}"


def go(x: int, y: int, z: int, speed: int):
    return f"go {x} {y} {z} {speed}"


def curve(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, speed: int):
    return f"curve {x1} {y1} {z1} {x2} {y2} {z2} {speed}"
