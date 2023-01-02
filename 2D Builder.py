import os

inv = [["Wood","Stone","Ground"],[50,50,0]]
tiles = ["@","%","#"]

def print_item(x):
	   print(f"{inv[0][x]}: {inv[1][x]}")
	
x = 2
y = 2
broke = " "
placed = " "
length = 14

world = [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
         [" "," ","#","#","#","#","#","#","#","#","#","#","#","#"," "," ",], 
         [" "," ","#","#","#","#","#","#","#","#","#","#","#","#"," "," ",],
         [" "," ","#","#","#","#","#","#","#","#","#","#","#","#"," "," ",],
         [" "," ","#","#","#","#","#","#","#","#","#","#","#","#"," "," ",],
         [" "," ","#","#","#","#","#","#","#","#","#","#","#","#"," "," ",],]

def print_map():
    print(f"{world[y-2][x-2]}{world[y-2][x-1]}{world[y-2][x]}{world[y-2][x+1]}{world[y-2][x+2]}")
    print(f"{world[y-1][x-2]}{world[y-1][x-1]}{world[y-1][x]}{world[y-1][x+1]}{world[y-1][x+2]}")
    print(f"{world[y][x-2]}{world[y][x-1]}{world[y][x]}{world[y][x+1]}{world[y][x+2]}")
    print(f"{world[y+1][x-2]}{world[y+1][x-1]}{world[y+1][x]}{world[y+1][x+1]}{world[y+1][x+2]}")
    print(f"{world[y+2][x-2]}{world[y+2][x-1]}{world[y+2][x]}{world[y+2][x+1]}{world[y+2][x+2]}")

while True:
    os.system("cls" if os.name == "nt" else "clear")
    world[y][x] = "$"
    print_map()
    print(f"Pos: X:{x-2} Y:{y-2} | '?' for help")
    
    action = input(">")
    
    if action == "a":
        if world[y][x-1] == " ":
            world[y][x] = " "
            x -= 1
    elif action == "d":
        if world[y][x+1] == " ":
            world[y][x] = " "
            x += 1
    elif action == "w":
        if world[y-1][x] == " " and world[y+1][x] != " ":
            world[y][x] = " "
            y -= 2
    elif action == "W":
        if world[y-1][x] == " " and world[y+1][x] != " ":
            world[y][x] = " "
            y -= 3
    elif action == "i":
        for i in range(len(inv)+1):
            print(f"{inv[0][i]}: {inv[1][i]}")
        input("Press ENTER to continue")
    elif action == "b":
        location = input("1, 2, 3 for top, 4 & 5 for sides, and 6, 7, 8 for bottom in that order\n>>")
        if location == "1":
            broke = world[y-1][x-1]
            world[y-1][x-1] = " "
        elif location == "2":
            broke = world[y-1][x]
            world[y-1][x] = " "
        elif location == "3":
            broke = world[y][x+1]
            world[y-1][x+1] = " "
        elif location == "4":
            broke = world[y][x-1]
            world[y][x-1] = " "
        elif location == "5":
            broke = world[y][x+1]
            world[y][x+1] = " "
        elif location == "6":
            broke = world[y+1][x-1]
            world[y+1][x-1] = " "
        elif location == "7":
            broke = world[y+1][x]
            world[y+1][x] = " "
        elif location == "8":
            broke = world[y+1][x+1]
            world[y+1][x+1] = " "
            
        if broke == "#":
            inv[1][2] += 1
        elif broke == "@":
            inv[1][0] += 1
        elif broke == "%":
            inv[1][1] += 1
    elif action == "p":
        location = input("1, 2, 3 for top, 4 & 5 for sides, and 6, 7, 8 for bottom in that order\n>>")
        place = int(input("1 = Wood (@), 2 = Stone (%), 3 = Ground (#)\n>>"))
        
        if location == "1":
            world[y-1][x-1] = tiles[place-1]
        elif location == "2":
            world[y-1][x] = tiles[place-1]
        elif location == "3":
            world[y-1][x+1] = tiles[place-1]
        elif location == "4":
            world[y][x-1] = tiles[place-1]
        elif location == "5":
            world[y][x+1] = tiles[place-1]
        elif location == "6":
            world[y+1][x-1] = tiles[place-1]
        elif location == "7":
            world[y+1][x] = tiles[place-1]
        elif location == "8":
            world[y+1][x+1] = tiles[place-1]
        
        inv[1][place-1] -= 1
        
    elif action == "?":
        print("Use A and D to move, W to jump (capital to jump higher), B to break, and P to place")
        input("Press ENTER to continue")
            
    if x == len(world[0])-2:
        x -= 1
    elif x == 1:
        x += 1
    
    if world[y+1][x] == " ":
        world[y][x] = " "
        y += 1
    
    if y > len(world)-3:
        y -= 1
    elif y == 1:
        y += 1
