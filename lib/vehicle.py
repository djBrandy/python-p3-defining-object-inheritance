class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
    pass

    def go (self):
        return "vrrrrrrrooom!"
    

    def fill_up_tank (self):
        return "filling up!"




wheel_size = Vehicle(48, 4)
