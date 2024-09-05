import math
from tabulate import tabulate

class Reflector:

## Deff Class Vars
    def __init__(self):
        self.flec_x = None
        self.flec_y = None
        self.refl = float(0.95) ## Predefined
        self.c = 7
        self.m = None
        self.n = None
        self.a = None
        self.Lux_initial = None
        self.distance = None
        self.L_source = None
        self.L_reflector = None
        self.L_0 = None
        self.feet = None
        self.z = 0.3048
        self.e = 1
        self.L_final = 0
        self.coordinates = []
        self.L_z = []
        self.x = None
        self.y = None
        self.r2 = None
        self.L = None
        self.L_cosine = None





    def getinputs(self):
        ## Inputs Reflector Size
        self.flec_x = int(input("Reflector Height (in meter): ")) # insert width
        self.flec_y = int(input("Reflector Width (in meter): ")) # insert height

        ## Predefined
        self.refl = float(0.95)

        ##Inputs Lux
        self.Lux_initial = float(input("Source luminance (in lux): ")) # insert the luminance of the source at the reflector

        ##Input Distance
        self.distance = int(input("Maximum distance from the reflector (in feet): "))
    
   
    def inputmath(self):

        ##Luminous Flux
        self.L_source = self.Lux_initial*self.flec_x*self.flec_y   # luminous flux
        print(self.L_source)

        ##Luminious Flux after Absorbption Cooefficient
        self.L_reflector = self.refl*self.L_source  
        print(self.L_reflector)

        ##Convert Distance to Feet
        self.feet = round(self.distance/3.28)
        print(self.distance)

        ##Number of Squares in X-dir
        self.m = self.flec_x*self.c          # number of squares in the x-direction (adjusted)
        ##Number of Squares in Y-dir
        self.n = self.flec_y*self.c           # number of squares in the y-direction (adjusted)

        ## Side length of a square 
        self.a = self.flec_x/self.m  

        ##Reflector
        ##self.L_0 = 2*self.L_reflector/(self.m*self.n)
        ##print(self.L_0)

        ## Diffuser - Light emits 360 from a point. 
        self.L_0 = self.L_reflector/(self.m*self.n)
        print(self.L_0)

        ##Convert Distance to Feet
        self.feet = round(self.distance/3.28)
        print(self.distance)

    ## Create Co-oridnates of each m'th and n'th point. 
    def coords(self):
        for i in range(0,self.m):
            self.x = -self.flec_x/2 + self.a/2 + i*self.a
            for j in range(0,self.n):
                self.y = -self.flec_y/2 + self.a/2 + j*self.a
                self.coordinates.append([self.x,self.y])

    ##Compute Luminance @ Z
    def lumaz(self):
        while self.e <= self.distance:
            self.L_final = 0 # Luminance at Point Z for each step. 
            for i in range(0, self.m*self.n):
                self.x = self.coordinates[i][0] # X Cords
                self.x = self.coordinates[i][1] # Y Cords
                self.r2 = self.x**2 + self.y**2 + self.z**2 # Square of R (pythagorean distance) between z point and pint x,y
                self.L = self.L_0/(4*math.pi*self.r2) ##Inverse Square Law

                ##Lamberts Cosine
                self.L_cosine = math.cos(math.pi-(math.acos(self.z/math.sqrt(self.r2)) + math.pi/2)) * self.L

                self.L_final += self.L_cosine # summing contributions from all point sources.
            self.L_z.append(self.L_final)
            self.z = self.z + 0.3048
            self.e = self.e + 1


        


def main():
    reflector = Reflector()
    reflector.getinputs()
    reflector.inputmath()
    reflector.coords()
    reflector.lumaz()
    table = [['Distance (feet)','Luminance (lux)']]
    for z in range (1, len(reflector.L_z) + 1):
        table.append([z,round(reflector.L_z[z-1])])

    print(tabulate(table, headers='firstrow', numalign="center"))



# Run the main function
if __name__ == "__main__":
    main()

   
