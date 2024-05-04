class Tello_Commands:
    def __init__(self) -> None:
        pass

    def command(self):
        return "command"
    
    def takeoff(self):
        return "takeoff"

    def land(self):
        return "land"
    
    def move_up(self, distance: int):
        return f"up {distance}"
    
    def move_down(self, distance: int):
        return f"down {distance}"
    
    def move_left(self, distance: int):
        return f"left {distance}"
    
    def move_right(self, distance: int):
        return f"right {distance}"
    
    def move_forward(self, distance: int):
        return f"forward {distance}"
    
    def move_back(self, distance: int):
        return f"back {distance}"
    
    def flip(self, direction: str):
        return f"flip {direction}"
