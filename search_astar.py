def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))
    ]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid)
    )]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid)
    )]
    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h
    open = [[f, g, h, x, y]]
    found = False # flag that is set when search is complet
    resign = False # flag set if we can't find expand
    count = 0
    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[3]
            y = next[4]
            g = next[1]
            expand[x][y] = count
            count += 1
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
    for i in range(len(expand)):
        print expand[i]
    return expand
