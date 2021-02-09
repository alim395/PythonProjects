from country import Country

class CountryCatalogue:
    def __init__ (self, countryFile):
        self.countryCat = dict()
        f = open(countryFile, 'r', encoding='utf-8', errors='ignore')
        rawData = f.readlines()
        for n in range(1, len(rawData)):
            cName, cContinent, cPop, cArea = rawData[n].split('|')
            self.countryCat[cName] = Country(cName, cPop, cArea, cContinent)

    def setPopulationOfCountry(self,name,popu):
        (self.countryCat[name]).setPopulation(popu)

    def setAreaOfCountry(self,name,area):
        (self.countryCat[name]).setArea(area)

    def setContinentOfCountry(self,name,cont):
        (self.countryCat[name]).setContinent(cont)

    def findCountry(self,countryName):
        if countryName in (self.countryCat):
            return (self.countryCat[countryName])
        else:
            return None

    def addCountry(self,countryName,pop,area,cont):
        self.countryCat[countryName] = Country(countryName, pop, area, cont)

    def printCountryCatalogue(self):
        for c in (self.countryCat).values():
            print(c)

    def saveCountryCatalogue(self,fname):
        count = 0
        f = open(fname, "w")
        f.write("Country|Continent|Population|Area\n") # Writes Header
        for country in sorted(self.countryCat):
            count += 1
            name = str(self.countryCat[country].getName())
            cont = str(self.countryCat[country].getContinent())
            popu = str(self.countryCat[country].getPopulation())
            area = str(self.countryCat[country].getArea())
            print('{}|{}|{}|{}\n'.format(name,cont,popu,area))
            f.write('{}|{}|{}|{}\n'.format(name,cont,popu,area))
