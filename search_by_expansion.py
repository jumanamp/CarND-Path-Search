# -----------
# User Instructions:
#
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # search and find shortest path to goal
    # ----------------------------------------
    rows = len(grid)
    columns = len(grid[0])
    open_list = [[0] + init] # first element in open_list
    path = []
    while open_list:
        print("new open list {}".format(open_list))
        min_cost = min(list(item[0] for item in open_list))
        display(min_cost)
        for loc in open_list:
            cost = loc[0]
            if cost ==  min_cost:
                x = loc[1]
                y = loc[2]
                expand[x][y] = count
                open_list.remove(loc)
                for step in delta:
                    succ = [sum(elem) for elem in zip(loc[-2:], step)]
                    in_grid = (succ[0] < len(grid)) and (succ[1] < len(grid[0]))
                    in_grid = in_grid and (succ[0]>=0 and succ[1]>=0)
                    if in_grid:
                        if (grid[succ[0]][succ[1]] == 0):
                            new = [cost + 1] + succ
                            if new not in open_list:
                                open_list.append(new) # expand
                    if succ == goal:
                        path = [cost + 1] + succ
                        print('shortest path: {}'.format(path))
                        return path
    return 'fail'

def expand():
    # ----------------------------------------
    # search and find expansion values to shortest path
    # ----------------------------------------
    closed = [[0] * len(grid[0]) for i in grid]
    closed[init[0]][init[1]] = 1
    expand = [[-1] * len(grid[0]) for i in grid]
    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]
    expand[x][y] = g
    count = 0
    found = False # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = expand_counter
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 <
                        len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            count += 1 #equivavelent to: count = count + 1
return expand 
