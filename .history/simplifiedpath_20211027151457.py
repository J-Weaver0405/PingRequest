#The simplified Path Finding Problem
#Given an N  N×N matrix of blocks with a source upper left block, we want to find a path from the source to the destination(the lower right block). We can only move downwards and to the right. Also a path is given by 11 and a wall is given by 00.

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


'''
start at 0,0 
check right 
    see if right is equal to 0
check down

movements: downwards, rights
upper left block: 0,0 
lower right block: n,n
'''