from collections import deque
import heapq

from utils import inGrid

class State():
    def __init__(self, point: tuple[int, int],  cost: int, hueristic: int, total: int) -> None:
        # Create an empty list with items of type T
        self.point: tuple[int, int] = point
        self.huaristic: int = hueristic
        self.cost: int = cost
        self.total: int = cost + hueristic

    def __lt__(self, other) -> bool:
        return self.total < other.total

    def __eq__(self, other) -> bool:
        return self.total == other.total



def dfs(grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]) -> tuple[list[tuple[int, int]], int]:
    directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    discovered: set[tuple[int, int]] = set()
    discovered.add(start)
    pointParent: dict[tuple[int, int], tuple[int, int] | None]= {}
    pointParent[start] = None
    
    stack: list[tuple[int, int]] = [start]
    goalFound = False
    while stack:
        x, y  = stack.pop()
        for dx, dy in directions:
            newX = x + dx
            newY = y + dy
            if inGrid(grid, newX, newY) and grid[newX][newY] == 0 and (newX, newY) not in discovered:
                pointParent[(newX, newY)] = (x, y)
                discovered.add((newX, newY))
                if (newX, newY) == goal:
                    goalFound = True
                    break
                stack.append((newX, newY))
    
        if goalFound:
            break
        
    if not goalFound:
        return [], 0
    
    
    path = constructPath(pointParent, goal)
    return path, len(discovered)
        

        

    # def recurse(x: int, y: int) -> bool:
    #     if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]):
    #         return False
    #     if grid[x][y] == 1:
    #         return False
    #     if (x, y) in visited:
    #         return False


    #     visited.add((x, y))
    #     path.append((x, y))
    #     if (x, y) == goal:
    #         return True

    #     for direction in directions:
    #         newX = x + direction[0]
    #         newY = y + direction[1]
    #         if recurse(newX, newY):
    #             return True
    #     _ = path.pop()
    #     return False


    # _ = recurse(start[0], start[1])

    # return path


def bfs(grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]) -> tuple[list[tuple[int, int]], int]:
    q: deque[tuple[int, int]] = deque()
    q.append(start)

    discovered: set[tuple[int, int]] = set()
    discovered.add(start)
    pointParent: dict[tuple[int, int], tuple[int, int] | None]= {}
    pointParent[start] = None
    
    directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
    goalFound = False
    while len(q) > 0:
        x, y = q.popleft()
        for dx, dy in directions:
            newX = x + dx
            newY = y + dy
            if inGrid(grid, newX, newY) and grid[newX][newY] == 0 and (newX, newY) not in discovered:
                pointParent[(newX, newY)] = (x, y)
                discovered.add((newX, newY))
                if (newX, newY) == goal:
                    goalFound = True
                    break
                q.append((newX, newY))

        if goalFound:
            break

    if not goalFound:
        return [], 0

    path = constructPath(pointParent, goal)
    return path, len(discovered)

#A star is broken right now, TODO: fix later
def aStar(grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]) -> tuple[list[tuple[int, int]], int]:
    
    pq: list[State] = []
    visited: set[tuple[int, int]] = set()
    distance: dict[tuple[int, int], int] = {}
    distance[start] = 0

    pointParent: dict[tuple[int, int], tuple[int, int] | None] = {}
    pointParent[start] = None
    huarsitic: int = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    heapq.heappush(pq, State(point=start, cost=0, hueristic=huarsitic, total=huarsitic ) )

    directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]

    goalFound = False
    while pq:
        state = heapq.heappop(pq)
        if state.point in visited:
            continue
        visited.add(state.point)
        if state.point == goal:
            goalFound = True
            break
        (x, y), cost = state.point, state.cost
        for dx, dy in directions:
            newX, newY = x + dx, y + dy 
            newCost = cost + 1
            if inGrid(grid, newX, newY) and grid[newX][newY] == 0 and (newX, newY) not in visited:
                prevCost: int | None =  distance.get((newX, newY))
                if prevCost is None or newCost < prevCost:
                    pointParent[(newX, newY)] = (x, y)
                    distance[(newX, newY)] = newCost
                    newHuaristic = abs(newX - goal[0]) + abs(newY - goal[1])
                    newState = State(point=(newX, newY), cost=newCost, hueristic=newHuaristic, total=newCost + newHuaristic)
                    heapq.heappush(pq, newState)


    if not goalFound:
        return [], 0
        
    path = constructPath(pointParent, goal)
    return path, len(visited)
    
    
def constructPath(pointParent: dict[tuple[int, int], tuple[int, int] | None], goal: tuple[int, int]) -> list[tuple[int, int]]:
    ptr = goal
    path: list[tuple[int, int]] = []
    while ptr is not None:
        path.append(ptr)
        ptr = pointParent[ptr]
        
    path.reverse()
    return path