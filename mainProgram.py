import copy
import time
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
from mazeGenerator import createMaze
import traversals

def program(size: int, wallBreakPercent: float) -> None:
    result = createMaze(size, wallBreakPercent=wallBreakPercent/100)
    if result is None:
        return
        
    grid, start, end = result
        
    pathDFS, timeDFS, pointsExploredDFS = benchMarkDFS(grid, start, end)
    pathBFS, timeBFS, pointsExploredBFS = benchMarkBFS(grid, start, end)
    pathAStar, timeAStar, pointsExploredAStar = benchMarkAStar(grid, start, end)
    
    if size <= 150:
        plot_maze(grid, "Generated Maze")
        plot_solution(copy.deepcopy(grid), pathDFS, "Maze Solution (DFS)")
        plot_solution(copy.deepcopy(grid), pathBFS, "Maze Solution (BFS)")
        plot_solution(copy.deepcopy(grid), pathAStar, "Maze Solution (A*)")
    
    
    labels = ["DFS", "BFS", "A*"]
    
    plt.figure()
    plt.bar(labels, [len(pathDFS), len(pathBFS), len(pathAStar)])
    plt.xlabel("Traversal Algorithms")
    plt.ylabel("Length of Solution Path")
    plt.title("Solution Length")
    plt.show()
    
    plt.figure()
    plt.bar(labels, [timeDFS, timeBFS, timeAStar])
    plt.xlabel("Traversal Algorithms")
    plt.ylabel("Time Taken")
    plt.title("Execution Time")
    plt.show()
    
    plt.figure()
    plt.bar(labels, [pointsExploredDFS, pointsExploredBFS, pointsExploredAStar])
    plt.xlabel("Traversal Algorithms")
    plt.ylabel("Points Explored")
    plt.title("Points Explored")
    plt.show()
    
def benchMarkDFS(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int])-> tuple[list[tuple[int, int]], float, int]:
    first = time.perf_counter()
    path, pointsExplored = traversals.dfs(grid, start, end)
    after = time.perf_counter()
    return path, after - first, pointsExplored
    
def benchMarkBFS(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> tuple[list[tuple[int, int]], float, int]:
    first = time.perf_counter()
    path, pointsExplored = traversals.bfs(grid, start, end)
    after = time.perf_counter()
    return path, after - first, pointsExplored
    
def benchMarkAStar(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> tuple[list[tuple[int, int]], float, int]:
    first = time.perf_counter()
    path, pointsExplored = traversals.aStar(grid, start, end)
    after = time.perf_counter()
    return path, after - first, pointsExplored
    
def plot_solution(grid: list[list[int]], path: list[tuple[int, int]], title: str):
    for x, y in path:
        grid[x][y] = 2
    cmap = pltc.ListedColormap(['white', 'black', 'green'])
    
    plt.imshow(grid, cmap=cmap)
    plt.xticks([])  
    plt.yticks([])
    plt.title(title)
    plt.show()
    
def plot_maze(grid: list[list[int]], title: str):
    plt.imshow(grid, cmap='binary')   
    plt.xticks([])  
    plt.yticks([])
    plt.title(title)
    plt.show()