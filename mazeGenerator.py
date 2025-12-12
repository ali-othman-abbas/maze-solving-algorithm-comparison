    
from math import floor
from random import randint, shuffle
from utils import inGrid


def createMaze(d: int, wallBreakPercent: float) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]] | None:
    if d <= 1:
        return None
    #creates a grid of cells of dimension d, where d is the logical dimension.
    #Not the real dimension of the 2d array
    grid: list[list[int]] = _constructGrid(d)

    visited: set[tuple[int, int]] = set()
    #xcoordinates of a random x and y point on the 2d array
    randX: int = 2*randint(0, d - 1) + 1
    randY: int = 2*randint(0, d - 1) + 1
    
    stack: list[tuple[int, int]] = [(randX, randY)]
    
    directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        point = stack.pop()
        visited.add(point)
        x, y = point
        shuffle(directions)
        for direc in directions:
            newX, newY = x + 2*direc[0], y + 2*direc[1]
            if inGrid(grid, newX, newY) and (newX, newY) not in visited:
                #clear wall
                grid[x + direc[0]][y + direc[1]] = 0
                stack.append(point)
                stack.append((newX, newY))
                break
                
        
    
    #creating entry and exit
    grid[1][0] = 0
    grid[len(grid) - 2][len(grid[0]) - 1] = 0
    
    
    _breakWalls(grid, wallBreakPercent)
    
    #returns the grid, with entry and exit coordinates
    return (grid, (1, 0), (len(grid) - 2, len(grid[0]) - 1))

def _constructGrid(d: int) -> list[list[int]]:
    borderLen = d + d + 1
    grid = [[1 for _ in range(borderLen)] for _ in range(borderLen)]

    for i in range(1, borderLen, 2):
        for j in range(1, borderLen, 2):
            grid[i][j] = 0

    return grid
    
def _breakWalls(grid: list[list[int]], percentage: float):
    walls:list[tuple[int, int]] = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == 1:
                walls.append((i, j))
                
    wallsToDestroy: int = floor(len(walls) * percentage)
    if wallsToDestroy > len(walls):
        wallsToDestroy = len(walls)
    elif wallsToDestroy < 0:
        wallsToDestroy = 0
    
    while wallsToDestroy > 0:
        n = len(walls)
        randNum = randint(0, n - 1)
        walls[randNum], walls[n - 1] = walls[n - 1], walls[randNum]
        wall = walls.pop()
        grid[wall[0]][wall[1]] = 0
        wallsToDestroy = wallsToDestroy - 1