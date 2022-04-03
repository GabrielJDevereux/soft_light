
import math
from tabulate import tabulate

flec_x = int(input("Reflector Height (in meter): ")) # insert width
flec_y = int(input("Reflector Width (in meter): ")) # insert height

c = 7
m = flec_x*c          # number of squares in the x-direction (adjusted)
n = flec_y*c           # number of squares in the y-direction (adjusted)

Lux_initial = float(input("Source luminance (in lux): ")) # insert the luminance of the source at the reflector
L_source = Lux_initial*flec_x*flec_y   # luminous flux

max = int(input("Maximum distance from the reflector in meters: "))

L_reflector = 0.735*L_source  # reflectance value of 73.5%

L_0 = 2*L_reflector/(m*n)
""""
L_0 is the luminance of a single point source; factor 2 is there because point source emits light in all directions,
not just in one side of a plane (as is the case with a sheet reflector)
"""


a = flec_x/m          # side length of a single square ADJUSTED

coordinates = []  # coordinates of a center of each square

# creates a list of all coordinates ADJUSTED
for i in range(0,m):
    x = -flec_x/2 + a/2 + i*a
    for j in range(0,n):
        y = -flec_y/2 + a/2 + j*a
        coordinates.append([x,y])

L_z = []  # luminance at various points

# computes luminance at point z
for z in range(1,max + 1):
    L_final = 0  # luminance at point z
    for i in range(0, m*n):
        x = coordinates[i][0]   # x coordinate
        y = coordinates[i][1]   # y coordinate
        r2 = x ** 2 + y ** 2 + z ** 2 # square of a distance between the z point and point (x,y)
        L = L_0/(4*math.pi*r2)   # inverse square law
        L_final += L   # summing contributions from all point sources
    L_z.append(L_final)

# final value is rounded to 3 decimal points

table = [['Distance (m)', 'Luminance (lux)']]
for z in range(1,max + 1):
    table.append([z,round(L_z[z-1])])

print(tabulate(table, headers='firstrow', numalign="center"))

#By Gabriel Devereux
#Digital Imaging Technician
#gabjol@me.com | gabrieldevereux.com


