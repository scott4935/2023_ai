import random # for random action e.g.) gold, wumpus, pitch ...

# position value of agent
now_pos = [1,1]
# does the agent hold gold
hold_gold = 0
# dirction[right, up, left, down]
direction = [1, 0, 0, 0]

# turn_left
def turn_left():
    now_direction = direction.index(1)
    direction[now_direction] = 0
    direction[(now_direction + 1) % 4] = 1

# turn_right
def turn_right():
    now_direction = direction.index(1)
    direction[now_direction] = 0
    direction[now_direction - 1] = 1

# go_forward / 0 == go right, 1 == go up, 2 == go left, 3 == go down
def go_forward():
    match direction.index(1):
        case 0:
            now_pos[1] += 1
        case 1:
            now_pos[0] += 1
        case 2:
            now_pos[1] -= 1
        case 3:
            now_pos[0] -= 1

# make map and place gold, wumpus, pitch
def mk_map():
    # set gold position
    while(1):
        gold_pos = random.randint(8,28)
        if(7 <= gold_pos <= 10 or 13<= gold_pos <= 16 or 19 <= gold_pos <= 22 or 25 <= gold_pos <= 28):
            break

    # set wumpus and pitch position
    while True:
        wumpus = []
        pitch = []
        for i in range(0,36):
            if i == gold_pos or i == 7:
                continue
            if 0 <= i <= 6 or 11 <= i <= 12 or 17<= i <= 18 or 23 <= i <= 24 or 29 <= i < 36:
                continue
            rand_val = random.randrange(100)
            if rand_val < 10:
                wumpus.append(i)
                continue
            elif rand_val < 20:
                pitch.append(i)
        if (len(wumpus) != 0) and (len(pitch) != 0):
            break
    # make cave map
    cave_map = [[[0,0,0,0,0] for col in range(6)]for row in range(6)]
    cave_map[gold_pos // 6][gold_pos % 6][2] = 1

    # set stench
    for _ in wumpus:
        cave_map[_ // 6][_ % 6][0] = 1
        cave_map[_ // 6 - 1][_ % 6][0] = 1
        cave_map[_ // 6 + 1][_ % 6][0] = 1
        cave_map[_ // 6][_ % 6 - 1][0] = 1
        cave_map[_ // 6][_ % 6 + 1][0] = 1


    # set breeze
    for _ in pitch:
        cave_map[_ // 6][_ % 6][1] = 1
        cave_map[_ // 6 - 1][_ % 6][1] = 1
        cave_map[_ // 6 + 1][_ % 6][1] = 1
        cave_map[_ // 6][_ % 6 - 1][1] = 1
        cave_map[_ // 6][_ % 6 + 1][1] = 1

    # set bump
    for _ in range(6):
        cave_map[_][0][3] = 1
        cave_map[_][5][3] = 1
        cave_map[_][0][0] = 0
        cave_map[_][5][0] = 0
        cave_map[_][0][1] = 0
        cave_map[_][5][1] = 0

    for _ in range(6):
        cave_map[0][_][3] = 1
        cave_map[5][_][3] = 1
        cave_map[0][_][0] = 0
        cave_map[5][_][0] = 0
        cave_map[0][_][1] = 0
        cave_map[5][_][1] = 0

    return wumpus, pitch, gold_pos, cave_map
        

# main
if __name__ == "__main__":
    wumpus, pitch, gold_pos, cave_map = mk_map()
    # chk map and position ... etc
    while True:
        print(f"--------------------------------------\ninput test value\n[1] show cave map\n[2] turn left\n[3] turn right\n[4] go forward")
        match int(input()):
            case 1:
                print(f"{wumpus}, {pitch}, {gold_pos}")
                for j in reversed(range(6)):
                    for k in range(6):
                        print(cave_map[j][k],end="")
                    print()
            case 2:
                turn_left()
                print(direction)
            case 3:
                turn_right()
                print(direction)

#test