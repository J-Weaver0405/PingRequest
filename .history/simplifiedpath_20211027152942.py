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
        return True

    x,y = pos
    #check right
    
    y,x = pos
    #check down

    # else try looking right and below to see 
    return False

if __name__ == '__main__':
    MAZE = [ 
    [ 1 , 0 , 1, 0 , 0],
    [ 1 , 1 , 0, 1 , 0],
    [ 0 , 1 , 0, 1 , 0],
    [ 0 , 1 , 0, 0 , 0],
    [ 1 , 1 , 1, 1 , 1] 
    ]

    solveMaze(MAZE,(3,5), 5)
    