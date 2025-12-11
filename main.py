import time
from mazeGenerator import createMaze
import traversals


def main():
    size: int = int(input("Maze size: "))
    result = createMaze(size, wallBreakPercent=0.3)
    if result is None:
        return
        
    grid, start, end = result
    printGrid(grid, start, end, [])
    print()
        
    # path1: list[tuple[int, int]] = traversals.dfs(grid, start, end)
    path1 : list[tuple[int, int]] = traversals.dfs(grid, start, end)
    path2 : list[tuple[int, int]] = traversals.bfs(grid, start, end)
    
    print("dfs search:")
    printGrid(grid, start, end, path1)
    print()
    print("bfs search (optimal):")
    printGrid(grid, start, end, path2)
    
    
    
    
            
            
def printGrid(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int], solutionPath: list[tuple[int, int]]):
    unorderedPath = set(solutionPath)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) == start:
                print("S", end="")
            elif (x, y) == end:
                print("G", end="")
            elif (x, y) in unorderedPath:
                print("P", end="")
            elif grid[x][y] == 0:
                print(".", end="")
            elif grid[x][y] == 1:
                print("#", end="")
        print()
    
main()