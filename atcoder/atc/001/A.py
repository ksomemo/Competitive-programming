import sys


def main():
    start = 's'
    goal = 'g'
    wall = '#'
    road = '.'

    size_line = sys.stdin.readline().strip('\n')
    y_size, x_size = map(int, size_line.split(' '))
    reached = [[0 for _ in range(x_size)] for _ in range(y_size)]
    maze = []
    for y, l in enumerate(sys.stdin):
        fix_l = l.strip('\n')
        maze.append(fix_l)
        start_x = fix_l.find(start)
        goal_x = fix_l.find(goal)
        if start_x > -1:
            start_pos = (start_x, y)
        if goal_x > -1:
            goal_pos = (goal_x, y)

    def must_return(x, y):
        if not 0 <= x < x_size:
            return True
        if not 0 <= y < y_size:
            return True
        if reached[y][x] == 1:
            return True
        if reached[goal_pos[1]][goal_pos[0]] == 1:
            return True
        if maze[y][x] == wall:
            return True

        return False

    def search(x, y):
        if must_return(x, y):
            return
        reached[y][x] = 1
        if maze[y][x] == goal:
            return

        search(x + 1, y)
        search(x - 1, y)
        search(x, y + 1)
        search(x, y - 1)
    #search(start_pos[0], start_pos[1])

    stack = [(start_pos[0], start_pos[1])]
    while len(stack) > 0:
        x, y = stack.pop()
        if must_return(x, y):
            continue
        reached[y][x] = 1
        if maze[y][x] == goal:
            continue

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))

    if reached[goal_pos[1]][goal_pos[0]] == 1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
