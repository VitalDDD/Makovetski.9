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


class TextProcessor():
    def __init__(self, in_string,_punktiantian):
        self.in_string=in_string
        self._punktiantian = None
    @property
    def is_punktiantian(self, i_in_string):
        i=i_in_string
        if i== "." or i== "," or i==":" or i==";" or i=="?" or i=="!" or i=="-" or i=="(" or i==")" or i==" " "
            self._punktiantian=True
        else:
            self._punktiantian=False
        return self._punktiantian
    def get_clean_string(self, in_string):
        for i in self.in_string:
            if is_punktiantian(i)==True
                i=" "
            str_new+=i
        return str_new


class TextLoader():
    def __init__(self, __text_processor, __clean_string):
        self.__text_processor=TextProcessor()
        self.__clean_string=__clean_string
    @property
    def set_clean_text(self):
        self.__clean_string=self.__text_processor
        return self.__clean_string
    @property
    def clean_string(self):
        print("Text already cleared.")



class Parallelogram():
    def __init__(self, width, length):
        self.width=width
        self.length=length
    def get_area(self):
        return self.width*self.length
class Square(Parallelogram):
    def __init__(self):
        Parallelogram.__init__(self)
    def get_area(self):
        return self.length**2
