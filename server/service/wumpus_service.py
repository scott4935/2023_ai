import random # for random action e.g.) gold, wumpus, pitch ...

#########################################################################
#               ____    ____    _____    _    ____    _                 #
#              /  _ \  /   _\  /__ __\  / \  /  _ \  / \  /|            #
#              | / \|  |  /      / \    | |  | / \|  | |\ ||            #
#              | |-||  |  \__    | |    | |  | \_/|  | | \||            #
#              \_/ \|  \____/    \_/    \_/  \____/  \_/  \|            #
#                                                                       #
#########################################################################

# turn_left
def turn_left(direction):
    now_direction = direction.index(1)
    direction[now_direction] = 0
    direction[(now_direction + 1) % 4] = 1
    return direction

# turn_right
def turn_right(direction):
    now_direction = direction.index(1)
    direction[now_direction] = 0
    direction[now_direction - 1] = 1
    return direction

# go_forward / 0 == E, 1 == N, 2 == W, 3 == S
def go_forward(now_pos, direction):
    #global now_pos
    match direction.index(1):
        case 0:
            if(now_pos[0] < 4):
                now_pos[0] += 1
            else:
                print(f"bumped out!")
        case 1:
            if(now_pos[1] < 4):
                now_pos[1] += 1
            else:
                print(f"bumped out!")
        case 2:
            if(now_pos[0] > 1):
                now_pos[0] -= 1
            else:
                print(f"bumped out!")
        case 3:
            if(now_pos[1] > 1):
                now_pos[1] -= 1
            else:
                print(f"bumped out!")
    if cave_map[now_pos[1]][now_pos[0]][5] == 1 or cave_map[now_pos[1]][now_pos[0]][6] == 1:
        for _ in range(7):
            agent_map[now_pos[1]][now_pos[0]][_] = cave_map[now_pos[1]][now_pos[0]][_]
            agent_map[now_pos[1]][now_pos[0]][7] = 1
        print("u r dead....start with new agent")
        now_pos = [1,1]
        direction = [1, 0, 0, 0]
    else:
        for _ in range(7):
            agent_map[now_pos[1]][now_pos[0]][_] = cave_map[now_pos[1]][now_pos[0]][_]
        agent_map[now_pos[1]][now_pos[0]][7] = 1
    return now_pos, direction, agent_map


def go_east(now_pos, direction):
    # dirction[E, N, W, S]
    match direction.index(1):
        case 0:
            go_forward(now_pos, direction)
        case 1:
            turn_right(direction)
            go_forward(now_pos, direction)
        case 2:
            while direction.index(1) != 0:
                turn_right(direction)
            go_forward(now_pos, direction)
        case 3:
            turn_left(direction)
            go_forward(now_pos, direction)


def go_north(now_pos, direction):
    # dirction[E, N, W, S]
    match direction.index(1):
        case 0:
            turn_left(direction)
            go_forward(now_pos, direction)
        case 1:
            go_forward(now_pos, direction)
        case 2:
            turn_right(direction)
            go_forward(now_pos, direction)
        case 3:
            while direction.index(1) != 1:
                turn_left(direction)
            go_forward(now_pos, direction)

def go_west(now_pos, direction):
    # dirction[E, N, W, S]
    match direction.index(1):
        case 0:
            while direction.index(1) != 2:
                turn_left(direction)
            go_forward(now_pos, direction)
        case 1:
            turn_left(direction)
            go_forward(now_pos, direction)
        case 2:
            go_forward(now_pos, direction)
        case 3:
            turn_right(direction)
            go_forward(now_pos, direction)

def go_south(now_pos, direction):
    # dirction[E, N, W, S]
    match direction.index(1):
        case 0:
            turn_right(direction)
            go_forward(now_pos, direction)
        case 1:
            while direction.index(1) != 3:
                turn_right(direction)
            go_forward(now_pos, direction)
        case 2:
            turn_left(direction)
            go_forward(now_pos, direction)
        case 3:
            go_forward(now_pos, direction)

# grab the gold
def grab(now_pos):
    global hold_gold
    # reversed x,y ..... i cant know reason
    print(f"{now_pos[0]}, {now_pos[1]}, {gold_pos}\n{cave_map[now_pos[1]][now_pos[0]]}")
    if (cave_map[now_pos[1]][now_pos[0]][2] == 1):
        hold_gold = 1
        cave_map[now_pos[1]][now_pos[0]][2] = 0

# shoot arrow
def shoot(now_pos, direction):
    global arrows
    # dirction[E, N, W, S]
    global cave_map
    # [Stench, Breeze, Glitter, Bump, Scream, wumpus, pitch]
    # [0, 1, 2, 3, 4, 5, 6]
    print(arrows)
    if(arrows > 0):
        arrows -=1
        print(direction.index(1))
        match int(direction.index(1)):
            case 0:
                # y, x
                print(f"in case 0\n{cave_map[now_pos[1]][now_pos[0] + 1][5]}")
                if cave_map[now_pos[1]][now_pos[0] + 1][5] == 1:
                    cave_map[now_pos[1]][now_pos[0] + 1][5] = 0
                    cave_map[now_pos[1]+ 1][now_pos[0] + 1][0] = 0
                    cave_map[now_pos[1]][now_pos[0] + 1 + 1][0] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] + 1][0] = 0
                    cave_map[now_pos[1]][now_pos[0] - 1 + 1][0] = 0
                    #..done
                    if cave_map[now_pos[1]+ 1][now_pos[0] + 1][3] != 1:
                        cave_map[now_pos[1]+ 1][now_pos[0] + 1][4] = 1
                    if cave_map[now_pos[1]][now_pos[0] + 1 + 1][3] != 1:
                        cave_map[now_pos[1]][now_pos[0] + 1 + 1][4] = 1
                    if cave_map[now_pos[1] - 1][now_pos[0] + 1][3] != 1:
                        cave_map[now_pos[1] - 1][now_pos[0] + 1][4] = 1
                    if cave_map[now_pos[1]][now_pos[0] - 1 + 1][3] != 1:
                        cave_map[now_pos[1]][now_pos[0] - 1 + 1][4] = 1

            case 1:
                # y, x
                print(f"in case 1\n{cave_map[now_pos[1] + 1][now_pos[0]][5]}")
                if cave_map[now_pos[1] + 1][now_pos[0]][5] == 1:
                    cave_map[now_pos[1] + 1][now_pos[0]][5] = 0
                    cave_map[now_pos[1] + 1][now_pos[0] + 1][0] = 0
                    cave_map[now_pos[1] + 1 + 1][now_pos[0]][0] = 0
                    cave_map[now_pos[1] + 1][now_pos[0] - 1][0] = 0
                    cave_map[now_pos[1] + 1 - 1][now_pos[0]][0] = 0
                    #..done
                    if cave_map[now_pos[1] + 1][now_pos[0] + 1][3] != 1:
                        cave_map[now_pos[1] + 1][now_pos[0] + 1][4] = 1
                    if cave_map[now_pos[1] + 1 + 1][now_pos[0]][3] != 1:
                        cave_map[now_pos[1] + 1 + 1][now_pos[0]][4] = 1
                    if cave_map[now_pos[1] + 1][now_pos[0] - 1][3] != 1:
                        cave_map[now_pos[1] + 1][now_pos[0] - 1][4] = 1
                    if cave_map[now_pos[1] + 1 - 1][now_pos[0]][3] != 1:
                        cave_map[now_pos[1] + 1 - 1][now_pos[0]][4] = 1     
            case 2:
                # y, x
                print(f"in case 2\n{cave_map[now_pos[1]][now_pos[0] - 1][5]}")
                if cave_map[now_pos[1]][now_pos[0] - 1][5] == 1: 
                    cave_map[now_pos[1]][now_pos[0] - 1][5] = 0
                    cave_map[now_pos[1]][now_pos[0] - 1 + 1][0] = 0
                    cave_map[now_pos[1] + 1][now_pos[0] - 1][0] = 0
                    cave_map[now_pos[1]][now_pos[0] - 1 - 1][0] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] - 1][0] = 0
                    if cave_map[now_pos[1]][now_pos[0] - 1 + 1][3] != 1:
                        cave_map[now_pos[1]][now_pos[0] - 1 + 1][4] = 1
                    if cave_map[now_pos[1] + 1][now_pos[0] - 1][3] != 1:
                        cave_map[now_pos[1] + 1][now_pos[0] - 1][4] = 1
                    if cave_map[now_pos[1]][now_pos[0] - 1 - 1][3] != 1:
                        cave_map[now_pos[1]][now_pos[0] - 1 - 1][4] = 1
                    if cave_map[now_pos[1] - 1][now_pos[0] - 1][3] != 1:
                        cave_map[now_pos[1] - 1][now_pos[0] - 1][4] = 1 
            case 3:
                # y, x
                print(f"in case 3\n{cave_map[now_pos[1] - 1][now_pos[0]][5]}")
                if cave_map[now_pos[1] - 1][now_pos[0]][5] == 1:
                    cave_map[now_pos[1] - 1][now_pos[0]][5] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] + 1][0] = 0
                    cave_map[now_pos[1] - 1 + 1][now_pos[0]][0] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] - 1][0] = 0
                    cave_map[now_pos[1] - 1 - 1][now_pos[0]][0] = 0
                    if cave_map[now_pos[1] - 1][now_pos[0] + 1][3] != 1:
                        cave_map[now_pos[1] - 1][now_pos[0] + 1][4] = 1
                    if cave_map[now_pos[1] - 1 + 1][now_pos[0]][3] != 1:
                        cave_map[now_pos[1] - 1 + 1][now_pos[0]][4] = 1
                    if cave_map[now_pos[1] - 1][now_pos[0] - 1][3] != 1:
                        cave_map[now_pos[1] - 1][now_pos[0] - 1][4] = 1
                    if cave_map[now_pos[1] - 1 - 1][now_pos[0]][3] != 1:
                        cave_map[now_pos[1] - 1 - 1][now_pos[0]][4] = 1 
def climb(now_pos):
    global hold_gold
    if now_pos[0] == 1 and now_pos[1] == 1:
        if hold_gold == 1:
            print("clear!! bye bye~")
            exit()
        else:
            print("no! u dont have gold")
    else:
        print("nono~ go back to the base")
    
# make map and place gold, wumpus, pitch
def mk_map():
    global gold_pos
    # set gold position
    while(1):
        gold_pos = random.randint(8,28)
        if(7 <= gold_pos <= 10 or 13<= gold_pos <= 16 or 19 <= gold_pos <= 22 or 25 <= gold_pos <= 28):
            break

    # set wumpus and pitch position
    while True:
        global wumpus
        wumpus = []
        global pitch
        pitch = []
        for i in range(0,36):
            if i == gold_pos or i == 7:
                continue
            if 0 <= i <= 6 or 11 <= i <= 12 or 17<= i <= 18 or 23 <= i <= 24 or 29 <= i < 36:
                continue
            rand_val = random.randrange(0,100,1)
            if rand_val < 10:
                wumpus.append(i)
                continue
            elif rand_val < 20:
                pitch.append(i)
        if (len(wumpus) != 0) and (len(pitch) != 0):
            break
    # make cave map
    global cave_map
    # [Stench, Breeze, Glitter, Bump, Scream, wumpus, pitch]
    # [0, 1, 2, 3, 4, 5, 6]
    cave_map = [[[0,0,0,0,0,0,0] for col in range(6)]for row in range(6)]
    cave_map[gold_pos // 6][gold_pos % 6][2] = 1

    # make agent map
    global agent_map
    # [Stench, Breeze, Glitter, Bump, Scream, wumpus, pitch, visited]
    # [0, 1, 2, 3, 4, 5, 6, 7]
    agent_map = [[[0,0,0,0,0,0,0,0] for col in range(6)]for row in range(6)]

    # set stench
    for _ in wumpus:
        cave_map[_ // 6][_ % 6][5] = 1
        cave_map[_ // 6 - 1][_ % 6][0] = 1
        cave_map[_ // 6 + 1][_ % 6][0] = 1
        cave_map[_ // 6][_ % 6 - 1][0] = 1
        cave_map[_ // 6][_ % 6 + 1][0] = 1


    # set breeze
    for _ in pitch:
        cave_map[_ // 6][_ % 6][6] = 1
        cave_map[_ // 6 - 1][_ % 6][1] = 1
        cave_map[_ // 6 + 1][_ % 6][1] = 1
        cave_map[_ // 6][_ % 6 - 1][1] = 1
        cave_map[_ // 6][_ % 6 + 1][1] = 1

    # set bump
    for _ in range(6):
        cave_map[_][0][3] = 1
        cave_map[_][5][3] = 1
        agent_map[_][0][3] = 1
        agent_map[_][5][3] = 1
        cave_map[_][0][0] = 0
        cave_map[_][5][0] = 0
        cave_map[_][0][1] = 0
        cave_map[_][5][1] = 0

    for _ in range(6):
        cave_map[0][_][3] = 1
        cave_map[5][_][3] = 1
        agent_map[0][_][3] = 1
        agent_map[5][_][3] = 1
        cave_map[0][_][0] = 0
        cave_map[5][_][0] = 0
        cave_map[0][_][1] = 0
        cave_map[5][_][1] = 0
    
    agent_map[1][1][:7] = cave_map[1][1][:7]
    agent_map[1][1][7] = 1
        
def new_setting():
    now_pos = [1,1]
    # does the agent hold gold
    global hold_gold
    hold_gold = 0
    # dirction[E, N, W, S]
    direction = [1, 0, 0, 0]
    mk_map()
    global arrows
    arrows = 2

    settings = {}
    settings['now_pos'] = now_pos
    settings['hold_gold'] = hold_gold
    settings['direction'] = direction
    settings['agent_map'] = agent_map
    settings['arrows'] = arrows
    settings['act_list'] = []

    return settings


#########################################################################
#                    ____  _____ _____ _      _____                     #
#                   /  _ \/  __//  __// \  /|/__ __\                    #
#                   | / \|| |  _|  \  | |\ ||  / \                      #
#                   | |-||| |_//|  /_ | | \||  | |                      #
#                   \_/ \|\____\\____\\_/  \|  \_/                      #
#                                                                       #
#########################################################################

def exec_agent():
    # position value of agent
    now_pos = [1,1]
    # now_pos = [1,1]
    # does the agent hold gold
    global hold_gold
    hold_gold = 0
    # dirction[E, N, W, S]
    direction = [1, 0, 0, 0]
    # arrows(init val 2)
    global arrows
    arrows = 2
    # [Stench, Breeze, Glitter, Bump, Scream, wumpus, pitch, visited]
    # [0, 1, 2, 3, 4, 5, 6, 7]
    global agent_map
    # chk data
    print(now_pos)
    test = now_pos
    print(agent_map[now_pos[0]][now_pos[1]])

    # return queue
    for_return = []
    while True:
        for_return.append(now_pos)
        print(for_return)
        # chk bump
        can_forward_visited = [0, 0, 0, 0]
        can_forward_not_visited = [0, 0, 0, 0]
        # chk can forward east
        if agent_map[now_pos[1] + 1][now_pos[0]][3] != 1 and agent_map[now_pos[1] + 1][now_pos[0]][5] != 1 and agent_map[now_pos[1] + 1][now_pos[0]][6] != 1:
            if agent_map[now_pos[1] + 1][now_pos[0]][7] == 1:
                can_forward_visited[1] = 2
            elif agent_map[now_pos[1] + 1][now_pos[0]][7] == 0:
                can_forward_not_visited[1] = 2
        
        # chk can forward north
        if agent_map[now_pos[1]][now_pos[0] + 1][3] != 1 and agent_map[now_pos[1]][now_pos[0] + 1][5] != 1 and agent_map[now_pos[1]][now_pos[0] + 1][6] != 1:
            if agent_map[now_pos[1]][now_pos[0] + 1][7] == 1:
                can_forward_visited[0] = 1
            elif agent_map[now_pos[1]][now_pos[0] + 1][7] == 0:
                can_forward_not_visited[0] = 1
            
        # chk can forward west
        if agent_map[now_pos[1] - 1][now_pos[0]][3] != 1 and agent_map[now_pos[1] - 1][now_pos[0]][5] != 1 and agent_map[now_pos[1] - 1][now_pos[0]][6] != 1:
            if agent_map[now_pos[1] - 1][now_pos[0]][7] == 1:
                can_forward_visited[3] = 4
            elif agent_map[now_pos[1] - 1][now_pos[0]][7] == 0:
                can_forward_not_visited[3] = 4
        
        # chk can forward south
        if agent_map[now_pos[1]][now_pos[0] - 1][3] != 1 and agent_map[now_pos[1]][now_pos[0] - 1][5] != 1 and agent_map[now_pos[1]][now_pos[0] - 1][6] != 1:
            if agent_map[now_pos[1]][now_pos[0] - 1][7] == 1:
                can_forward_visited[2] = 3
            elif agent_map[now_pos[1]][now_pos[0] - 1][7] == 0:
                can_forward_not_visited[2] = 3

        print(can_forward_visited)
        print(can_forward_not_visited)
        forward_choice = 0

        not_visit_cnt = can_forward_not_visited.count(0)
        if not_visit_cnt != 4:
            while forward_choice == 0:
                forward_choice = random.sample(can_forward_not_visited, 1)
                forward_choice = forward_choice[0]
        else:
            while forward_choice == 0:
                forward_choice = random.sample(can_forward_visited, 1)
                forward_choice = forward_choice[0]

        print(forward_choice)

        match forward_choice:
            case 1:
                go_east(now_pos, direction)
            case 2:
                go_north(now_pos, direction)
            case 3:
                go_west(now_pos, direction)
            case 4:
                go_south(now_pos, direction)

        input()

#########################################################################
#                   _          ____      _      _                       #
#                  / \__/|    /  _ \    / \    / \  /|                  #
#                  | |\/||    | / \|    | |    | |\ ||                  #
#                  | |  ||    | |-||    | |    | | \||                  #
#                  \_/  \|    \_/ \|    \_/    \_/  \|                  #
#                                                                       #
#########################################################################

if __name__ == "__main__":
    # position value of agent
    now_pos = [1,1]
    # does the agent hold gold
    global hold_gold
    hold_gold = 0
    # dirction[E, N, W, S]
    direction = [1, 0, 0, 0]
    mk_map()
    # arrows(init val 2)
    global arrows
    arrows = 2
    # chk map and position ... etc
    while True:
        print(f"--------------------------------------\ninput test value\n[0] now position\n[1] show cave map\n[2] turn left")
        print(f"[3] turn right\n[4] go forward\n[5] grab the gold\n[6] shoot\n[7] show agent map")
        print(f"[8] climb\n[9] execute agent")
        match int(input()):
            case 0:
                print(f"{now_pos[0]}, {now_pos[1]}, {cave_map[now_pos[1]][now_pos[0]]}")
            case 1:
                print(f"{wumpus}, {pitch}, {gold_pos}")
                for j in reversed(range(6)):
                    for k in range(6):
                        print(cave_map[j][k],end="")
                    print()
                # print(f"{wumpus}, {pitch}, {gold_pos}")
                # for j in reversed(range(6)):
                #     for k in (range(6)):
                #         print(cave_map[j][k][2],end="")
                #     print()
            case 2:
                turn_left(direction)
                print(direction)
            case 3:
                turn_right(direction)
                print(direction)
            case 4:
                match int(input("[1] east\n[2] north\n[3] west\n[4] south\n")):
                    case 1:
                        go_east(now_pos, direction)
                    case 2:
                        go_north(now_pos, direction)
                    case 3:
                        go_west(now_pos, direction)
                    case 4:
                        go_south(now_pos, direction)
                print(f"{now_pos}\n{cave_map[now_pos[1]][now_pos[0]]}\n")
            case 5:
                grab(now_pos)
                print(hold_gold)
            case 6:
                shoot(now_pos, direction)
                print("shoot done")
            case 7:
                for j in reversed(range(6)):
                    for k in range(6):
                        print(agent_map[j][k],end="")
                    print()
            case 8:
                climb()
            case 9:
                exec_agent()