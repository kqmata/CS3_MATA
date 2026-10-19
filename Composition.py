class Room:
    def __init__(self, name: str):
        self.name = name

class House:
    def __init__(self):
        # The House creates and owns these Room objects directly inside its constructor
        self.rooms = [Room("Kitchen"), Room("Bedroom")]

# 1. Instantiate the parent object
my_house = House()

# 2. Iterate through the child objects (Rooms) created internally
for room in my_house.rooms:
    print(f"Room created: {room.name}")