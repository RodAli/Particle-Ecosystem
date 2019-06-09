import random

# Should make this into a static class 
class Colours: 
    
    def __init__(self):
        self.colour_list = {
            "BLACK":  (0, 0, 0),
            "WHITE": (255, 255, 255),
            "GREEN": (0, 255, 0),
            "RED": (255, 0, 0),
            "BLUE": (0, 0, 255)
        }

    # This class should avoid returning black? we dont want black dots ...
    def getRandomColor(self):
        return random.choice(list(self.colour_list.values())) 