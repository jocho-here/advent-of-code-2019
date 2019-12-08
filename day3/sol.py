def draw_wires(input_grid, line, wire_num):
    intersections = []
    pos = [0,0]
    steps = 0

    for point in line:
        direction = point[0]
        length = int(point[1:])

        if direction == 'U':
            for i in range(1, length+1):
                if pos[1]+i not in input_grid[pos[0]]:
                    input_grid[pos[0]][pos[1]+i] = {wire_num: steps + i}
                elif wire_num not in input_grid[pos[0]][pos[1]+i]:
                    intersections.append((pos[0], pos[1]+i))
                    input_grid[pos[0]][pos[1]+i][wire_num] = steps + i
            pos[1] += length
        elif direction == 'D':
            for i in range(1, length+1):
                if pos[1]-i not in input_grid[pos[0]]:
                    input_grid[pos[0]][pos[1]-i] = {wire_num: steps + i}
                elif wire_num not in input_grid[pos[0]][pos[1]-i]:
                    intersections.append((pos[0], pos[1]-i))
                    input_grid[pos[0]][pos[1]-i][wire_num] = steps + i
            pos[1] -= length
        elif direction == 'L':
            for i in range(1, length+1):
                if pos[0]-i not in input_grid:
                    input_grid[pos[0]-i] = {}
                if pos[1] not in input_grid[pos[0]-i]:
                    input_grid[pos[0]-i][pos[1]] = {wire_num: steps + i}
                elif wire_num not in input_grid[pos[0]-i][pos[1]]:
                    intersections.append((pos[0]-i, pos[1]))
                    input_grid[pos[0]-i][pos[1]][wire_num] = steps + i
            pos[0] -= length
        elif direction == 'R':
            for i in range(1, length+1):
                if pos[0]+i not in input_grid:
                    input_grid[pos[0]+i] = {}
                if pos[1] not in input_grid[pos[0]+i]:
                    input_grid[pos[0]+i][pos[1]] = {wire_num: steps + i}
                elif wire_num not in input_grid[pos[0]+i][pos[1]]:
                    intersections.append((pos[0]+i, pos[1]))
                    input_grid[pos[0]+i][pos[1]][wire_num] = steps + i
            pos[0] += length
        steps += length

    rtn_val = {
        'intersections': intersections,
        'input_grid': input_grid,
    }

    return rtn_val

def get_closest_intersection(points):
    closest_length = abs(points[0][0]) + abs(points[0][1])
    closest_point = points[0]

    for point in points[1:]:
        curr_length = abs(point[0]) + abs(point[1])

        if curr_length < closest_length:
            closest_length = curr_length
            closest_point = point

    return closest_point

def get_shortest_steps(input_grid, points):
    fewest_steps = sum(input_grid[points[0][0]][points[0][1]].values())

    for point in points[1:]:
        combined_steps = sum(input_grid[point[0]][point[1]].values())

        if combined_steps < fewest_steps:
            fewest_steps = combined_steps

    return fewest_steps

file_name = 'input.txt'
lines = [line.strip().split(',') for line in open(file_name, 'r').readlines()]
initial_grid = {0:{0:True}}

result = draw_wires(initial_grid, lines[0], 1)
result = draw_wires(result['input_grid'], lines[1], 2)

#point = get_closest_intersection(result['intersections'])
#print(abs(point[0])+abs(point[1]))
print(get_shortest_steps(result['input_grid'], result['intersections']))
