import random
class Dot:

    def __init__(self, id, x, y, radius, speed, colour):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
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
        self.x += self.speed
    
    def moveLeft(self):
        self.x -= self.speed
    
    def moveUp(self):
        self.y -= self.speed
    
    def moveDown(self):
        self.y += self.speed
    
    def isOutsideBounds(position, radius, board_width, board_height):
        return position[0] - radius < 0 or position[0] + radius > board_width - 1 or position[1] - radius < 0 or position[1] + radius > board_height - 1
    
    def moveRandom(self, board_width, board_height):
        possibleMoves = []

        if not Dot.isOutsideBounds((self.x - self.speed, self.y), self.radius, board_width, board_height):
            possibleMoves.append(self.moveLeft)
        if not Dot.isOutsideBounds((self.x + self.speed, self.y), self.radius, board_width, board_height):
            possibleMoves.append(self.moveRight)
        if not Dot.isOutsideBounds((self.x, self.y - self.speed), self.radius, board_width, board_height):
            possibleMoves.append(self.moveUp)
        if not Dot.isOutsideBounds((self.x, self.y + self.speed), self.radius, board_width, board_height):
            possibleMoves.append(self.moveDown)

        if len(possibleMoves) > 0:
            random.choice(possibleMoves)()
    
    # def moveRandom(self, board_width, board_height):
    #     # Get possible moves to take
    #     possible_moves = []
    #     if self.x > 0:
    #         possible_moves.append(self.moveLeft)
        
    #     if self.x < board_width - 1:
    #         possible_moves.append(self.moveRight)
        
    #     if self.y > 0:
    #         possible_moves.append(self.moveUp)
        
    #     if self.y < board_height - 1:
    #         possible_moves.append(self.moveDown)
        
    #     # Make the move
    #     random.choice(possible_moves)()

    #     # Based on the speed, if the move brings us over the boundaries, bring back in bounds
    #     if self.x < 0:
    #         self.x = self.radius - 1
        
    #     if self.x > board_width - 1:
    #         self.x = board_width - self.radius

    #     if self.y < 0: 
    #         self.y = self.radius - 1

    #     if self.y > board_height - 1:
    #         self.y = board_height - self.radius