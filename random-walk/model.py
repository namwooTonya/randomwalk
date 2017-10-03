import random


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def distance(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return f'{self.x} {self.y}'


class Drunk:
    def __init__(self, name):
        self.name = name

    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)

    def __str__(self):
        return ('I am ' + self.name)


class Field:
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

    def getLoc(self, drunk):
        return self.drunks[drunk]

def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return (start.distance(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    namwoo = Drunk('namwoo')
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(namwoo, origin)
        distances.append(walk(f, namwoo, numSteps))
    return distances

def drunkTest(numTrials):
    for numSteps in [10, 100, 1000, 10000, 100000]:
        distances = simWalks(numSteps, numTrials)
        print (f'Random walk of {numSteps} steps')
        print (f'Mean = {sum(distances)/len(distances)}')
        print (f'Max = {max(distances)} Min = {min(distances)}')


drunkTest(10)
