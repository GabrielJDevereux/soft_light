
import math
from tabulate import tabulate

flec_x = int(input("Reflector Height (in meter): ")) # insert height
flec_y = int(input("Reflector Width (in meter): ")) # insert width
meters = int(input("Maximum distance from the reflector in meters:")) # Distance

def triangle_angle(b_o, a):
    b = b_o / 2
    alpha_degrees = math.atan(a/b) * 180 / math.pi   #Calculating angle reflector outward
    
    beta_degrees = math.atan(b/a) * 180 / math.pi   * 2 #Calculating point of farthest conversion

    return(beta_degrees)

def soft_angle(angle):
    large_radius = ((1+math.sin(math.radians(angle/2))) / (math.sin(math.radians(angle/2)))) * 0.08 #Large Radius of theoretical circle
    tangent = math.sqrt(large_radius**2-2*large_radius*0.08) #the distance from apex to tangent

    hypo_apex = tangent**2 + 0.08**2 #calculating the hypotenuse of the apex (pythag)
    hypo_apex = math.sqrt(hypo_apex) #pythag2

    innercirc = math.asin(tangent/hypo_apex) * 180 / math.pi #The angle of triangle in circle
    soft_light_cover = (180-innercirc) * 2 #The angle of light hitting sphere

    return(soft_light_cover)
    
table = [['Distance (m)', 'Verticle Cover', 'Horizontal Cover',]]

for i in range(0, meters):
    table.append([i+1, round(soft_angle(triangle_angle(flec_x, i+1)),4), round(soft_angle(triangle_angle(flec_y, i+1)),4) ])

print("")
print(tabulate(table, headers='firstrow', numalign="center"))


#Gabriel Devereux
#DIT, gabrieldevereux.com
#gabjol@me.com
