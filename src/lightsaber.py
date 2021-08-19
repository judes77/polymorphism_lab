from src.prop import Prop

class Lightsaber(Prop):
    
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "whoooosh"
