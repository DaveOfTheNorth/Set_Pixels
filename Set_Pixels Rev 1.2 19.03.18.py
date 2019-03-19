cord1 = [1,5]
cord2 = [3,2]

def rngpts(cord1, cord2):
    corner1 = [min(cord1[0], cord2[0]), min(cord1[1],cord2[1])]
    corner2 = [max(cord1[0], cord2[0]), max(cord1[1],cord2[1])]
    coord = [min(cord1[0], cord2[0]), min(cord1[1],cord2[1])]
    pixels=[]
    x = coord[0]
    y = coord[1]
    while x <= corner2[0] & y <= corner2[1]:
        while y <= corner2[1]:
            print(coord)
            y += 1
            pixels.append((x,y))
            print(corner2[1],pixels)
        print(pixels)
        x += 1                          
        y = coord[1]
        
        
   
rngpts(cord1, cord2)