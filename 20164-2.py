def mark(coordinates,plate):
    for i in range(4):
        plate[coordinates[i][0]][coordinates[i][1]] = 1

def print_plate(plate):
    x = len(plate)
    y = len(plate[0])
    for i in range(x):
        for j in range(y):
            print(plate[i][j], end = ' ')
        print()

def move(coordinates):
    for i in range(4):
        coordinates[i][0] +=1
        
def wrap_up():
    plate = []
    block = []
    coordinates = []
    for i in range(15):
        plate.append(list(map(int,input().split())))
    
    for i in range(4):
        block.append(list(map(int,input().split())))
    lstart = int(input())
    for i in range(4):
        for j in range(4):
            if block[i][j]:
                coordinates.append([i,j+lstart-1])
    marked = 0
    while True:
        flag = 0
        for i in range(3,-1,-1):
            if coordinates[i][0] < 14 and plate[coordinates[i][0]+1][coordinates[i][1]] == 0:
                flag+=1
            else:
                mark(coordinates,plate)
                marked = 1
                print_plate(plate)
                break
            if flag == 4:
                move(coordinates)
        if marked:
            break

wrap_up()
            
    
