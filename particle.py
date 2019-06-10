import random
class Particle:

    def __init__(self, id, x, y, colour):
        self.id = id
        self.x = x
        self.y = y
        self.colour = colour

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def getLocation(self):
        return (self.x, self.y)

    def setLocation(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def getColour(self):
        return self.colour
    
    def moveRight(self):
        self.x += 1
    
    def moveLeft(self):
        self.x -= 1
    
    def moveUp(self):
        self.y -= 1
    
    def moveDown(self):
        self.y += 1
    
    def getViableMoves(self, boardWidth, boardHeight):
        possibleMoves = []

        if self.x > 0:
            possibleMoves.append(self.moveLeft)
        if self.x < board_width - 1:
            possibleMoves.append(self.moveRight)
        if self.y > 0:
            possibleMoves.append(self.moveUp)
        if self.y < board_height - 1:
            possibleMoves.append(self.moveDown)

        return possibleMoves

    def moveRandom(self, board_width, board_height):
        # TODO: 
        viableMoves = 

        if len(possibleMoves) > 0:
            random.choice(possibleMoves)()
