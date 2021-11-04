"""
The Simplified Path Finding Problem
Given an N  N×N matrix of blocks with a source upper left block, we want to find a path from the source to the destination(the lower right block). We can only move downwards and to the right. Also a path is given by 11 and a wall is given by 00.

{ 
    { 1 , 0 , 1, 0 , 0},
    { 1 , 1 , 0, 1 , 0},
    { 0 , 1 , 0, 1 , 0},
    { 0 , 1 , 0, 0 , 0},
    { 1 , 1 , 1, 1 , 1} 
}

maze = [ 
    [ 1 , 0 , 1, 0 , 0],
    [ 1 , 1 , 0, 1 , 0],
    [ 0 , 1 , 0, 1 , 0],
    [ 0 , 1 , 0, 0 , 0],
    [ 1 , 1 , 1, 1 , 1] 
]

base case: we have arrived at the end (n, n -> 4,4)

if we have arrived at the end of the grid, 
    return true 
else:
    start at 0,0 
    check right 
        see if right is equal to 0 
    check down 
        see if it is equal to 0 

movements: downwards, rights
upper left block: 0,0 
lower right block: n - 1,n - 1
"""        

def solveMaze(MAZE, pos, N):
    
    # base case: we have arrived at the end
    if pos == (N - 1, N - 1):
        print("we have arrived at the end!")
        return [(N - 1, N - 1)]

    x,y = pos
    # check right 
    if x + 1 < N and MAZE[x + 1][y] == 1:
        next_step = solveMaze(MAZE, (x+1, y), N)
        if next_step != None:
            print(f"checking right at {next_step}")
            return [(x, y)] + next_step
            
    # check down 
    # 0,1
    if y + 1 < N and MAZE[x][y + 1] == 1:
       next_step = solveMaze(MAZE, (x, y + 1), N)
       if next_step != None:
            print(f"checking below at {next_step}")
            return [(x, y)] + next_step
    
    # else try looking right and below to see 
    return None

if __name__ == '__main__':
    MAZE = [ 
    [ 1 , 0 , 1, 0 , 0],
    [ 1 , 1 , 0, 1 , 0],
    [ 0 , 1 , 0, 1 , 0],
    [ 0 , 1 , 0, 0 , 0],
    [ 1 , 1 , 1, 1 , 1] 
    ]

print(solveMaze(MAZE,(0,0), 5))
    