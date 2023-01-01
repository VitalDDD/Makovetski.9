class Auto():

    def __init__(self, brand, сolour, engine_volume):
        self.brand = brand
        self.сolour = сolour
        self.engine_volume = engine_volume
        self.position_transmission = None
        self.brake_position = None

    def go_forward(self, position_transmission, brake_position):
        if self.position_transmission > 0 and self.brake_position==0:
            print("You are moving forward.")
        else:
            print("Take your foot off the brake pedal and shift into gear.")

    def go_back(self, position, brake_position):
        if self.position_transmission < 0 and self.brake_position == 0:
            print("You are moving back.")
        else:
            print("Take your foot off the brake pedal and engage reverse gear.")


class Auto_NF(Auto):

    def __init__(self, rudder_position):
        Auto.__init__(self)
        self.rudder_position=rudder_position

    def right_turn(self, rudder_position):
        if self.rudder_position > 0:
            print("You turn right.")
        elif self.rudder_position == 0:
            print("You are moving straight.")
        else:
            print("You turn left.")