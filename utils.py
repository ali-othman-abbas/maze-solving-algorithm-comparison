
def inGrid(grid: list[list[int]], x: int, y: int) -> bool:
   return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])