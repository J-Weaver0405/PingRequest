"""
Given a cost matrix cost[][] and a position (m, n) 
in cost[][], 

write a function that returns cost of minimum cost path 
to reach (m, n) from (0, 0). 

Each cell of the matrix represents a cost 
to traverse through that cell. 
The total cost of a path to reach (m, n) is the sum of all the costs on that path (including both source and destination). 
You can only traverse down, right and diagonally lower cells from a given cell, i.e., 
from a given cell (i, j), cells (i+1, j), (i, j+1), and (i+1, j+1) can be traversed. 
You may assume that all costs are positive integers.

For example, in the following figure, what is the minimum cost path to (2, 2)? 

Find the least cost path (add all the entries to find the least sum)

"""
import random
from pprint import pprint

graph = [[9, 9, 3]
[6, 8, 2]
[3, 1, 3]]

def generate_graph(n):

	graph = [[random.randint(1, 9) for i in range(n)] for i in range(n)]
	return graph

#diagonal m + 1, n + 1
# below m + 1 , n
# to the right m, n + 1,
 

def find_min_cost(graph, m , n):
    if (n < 0 or m < 0):
        return 0
    elif (m == 0 and n == 0):
        print('we are at the end')
        return graph [m] [n]
    else:
        return graph [m] [n] + min(
            find_min_cost(graph, m-1, n-1),
            find_min_cost(graph, m-1, n),
            find_min_cost(graph, m, n-1))
def min( x, y, z):
    if x < y:
        return x if (x<z) else z
    else:
        return y if (y<z) else z

 

if __name__ == '__main__':
	# graph = generate_graph(3)
	# for row in graph:
	# 	print(row)
	pass