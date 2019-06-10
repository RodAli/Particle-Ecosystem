import random

# Should make this into a static class 
class Colours: 
    
    def __init__(self):
        self.colourMap = {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "GREEN": (0, 255, 0),
            "RED": (255, 0, 0),
            "BLUE": (0, 0, 255)
        }
    
    def getColour(self, colourName):
        return self.colourMap[colourName]