class Door():
    def open_door(self):
        self.is_open = "is_opened"
        print("the door is open")
    def close_door(self):
        print("the door is closed")


class BlockedDoor(Door):
    def open_door(self):
        print("A door canot be opened and closed at the same time")
    def close_door(self):
        print("A door canot be opened and closed at the same time")

dooor = BlockedDoor()
print(dooor.open_door())