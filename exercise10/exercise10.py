import math
import os
import random
import re
import sys

def minimumMoves(grid, queue, goal, move, path):

    if len(queue) == 0:
        return False


    current_move = move[0]
    position = queue[0]
    del move[0]
    del queue[0]

    positionX = position[0]
    positionY = position[1]

    row = grid[positionY]
    column = []
    for y in grid:
        column.append(y[positionX])

    column_limit = search_limit(column, positionY)
    row_limit = search_limit(row, positionX)

    # Check if are new_moves and add in queue
    for x in range (row_limit[0], row_limit[1]):
        new_move = x, positionY
        if new_move not in path:
            if new_move == goal:
                return current_move + 1

            move.append(current_move + 1)
            queue.append(new_move)
            path.add(new_move)

    for y in range (column_limit[0], column_limit[1]):
        new_move = positionX, y
        if new_move not in path:
            if new_move == goal:
                return current_move + 1

            move.append(current_move + 1)
            queue.append(new_move)
            path.add(new_move)

    return minimumMoves(grid, queue, goal, move, path)

def search_limit(line, point):
    # Return the limit of the move in that line starting in point

    line_down = line[0:point]
    line_up = line[point:-1]

    if 'x' in line_down:
        reverse_line_down = line_down[::-1]
        down_limit = len(line_down) - reverse_line_down.index('x')

    else:
        down_limit = 0

    if 'x' in line_up:
        up_limit = point + line_up.index('x')

    else:
        up_limit = len(line)

    return down_limit, up_limit

def main():
    # Main Code
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])
    startY = int(startXStartY[1])

    start = [(startX, startY)]

    goalX = int(startXStartY[2])
    goalY = int(startXStartY[3])

    goal = (goalX, goalY)
    move = [0]
    path = set(start)

    result = minimumMoves(grid, start, goal, move, path)
    print(result)

if __name__ == '__main__':
    main()
