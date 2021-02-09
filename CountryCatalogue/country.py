class Country:
    def __init__(self, name, pop, area, continent):
        self.name = name
        self.pop = pop
        self.area = area
        self.continent = continent

    def getName(self):
        return str((self.name)).strip('\n')

    def getPopulation(self):
        return str((self.pop)).strip('\n')

    def getArea(self):
        return str((self.area)).strip('\n')

    def getContinent(self):
        return str(self.continent).strip('\n')

    def setPopulation(self, pop):
        pop = pop.strip('\n')
        self.pop = pop

    def setArea(self, area):
        area = area.strip('\n')
        self.area = area

    def setContinent(self, continent):
        continent = continent.strip('\n')
        self.continent = continent

    def __repr__(self):
        return str('{} (pop:{}, size:{}) in {}'.format(self.name, self.pop, self.area, self.continent))
