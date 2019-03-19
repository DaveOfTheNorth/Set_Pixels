import unicornhathd as uh
uh.rotation(90)

cord1 = [1,9]
cord2 = [8,2]

def rngpts(cord1, cord2):
    corner1 = [min(cord1[0], cord2[0]), min(cord1[1],cord2[1])]
    corner2 = [max(cord1[0], cord2[0]), max(cord1[1],cord2[1])]
    coord = [min(cord1[0], cord2[0]), min(cord1[1],cord2[1])]
    pixels=[]
    x = coord[0]
    y = coord[1]
    while ((x <= corner2[0]) and y <= (corner2[1] + 1)):
        while y <= corner2[1]:
            #print(coord)
            pixels.append((x,y))
            y += 1
            #print(corner2[0], x, corner2[1],y,pixels)
        x += 1                          
        y = coord[1]
    return pixels
        
   
points = rngpts(cord1, cord2)

print(points)

for x in range(len(points)):
    uh.set_pixel(points[x], 123, 200, 100)
    
uh.show()