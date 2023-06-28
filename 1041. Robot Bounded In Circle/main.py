def isRobotBounded(instructions):
    rotation, position = 0, [0, 0]

    instructions = instructions.replace('L', 'RRR')
    while 'RRRR' in instructions:
        instructions = instructions.replace('RRRR', '')
    for j in range(4):
        for i in instructions:
            if i == "R":
                rotation += 90
            if i == "G":
                if rotation % 360 == 0:
                    position[1] += 1
                elif abs(rotation) % 360 == 180:
                    position[1] -= 1
                elif abs(rotation) % 360 == 270:
                    position[0] -= 1
                elif abs(rotation) % 360 == 90:
                    position[0] += 1
        if position == [0, 0]:
            return True
    return False