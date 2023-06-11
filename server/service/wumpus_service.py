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
    global agent_map
    #global now_pos
    match direction.index(1):
        case 0:
            if(now_pos[0] < 4):
                now_pos[0] += 1
            else:
                print(f"bumped out!")
                agent_map[now_pos[1]][now_pos[0] + 1][3] = 1
                agent_map[now_pos[1]][now_pos[0] + 1][7] = 1
        case 1:
            if(now_pos[1] < 4):
                now_pos[1] += 1
            else:
                print(f"bumped out!")
                agent_map[now_pos[1] + 1][now_pos[0]][3] = 1
                agent_map[now_pos[1] + 1][now_pos[0]][7] = 1
        case 2:
            if(now_pos[0] > 1):
                now_pos[0] -= 1
            else:
                print(f"bumped out!")
                agent_map[now_pos[1]][now_pos[0] - 1][3] = 1
                agent_map[now_pos[1]][now_pos[0] - 1][7] = 1
        case 3:
            if(now_pos[1] > 1):
                now_pos[1] -= 1
            else:
                print(f"bumped out!")
                agent_map[now_pos[1] - 1][now_pos[0]][3] = 1
                agent_map[now_pos[1] - 1][now_pos[0]][7] = 1
    if cave_map[now_pos[1]][now_pos[0]][5] == 1 or cave_map[now_pos[1]][now_pos[0]][6] == 1:
        for _ in range(7):
            agent_map[now_pos[1]][now_pos[0]][_] = cave_map[now_pos[1]][now_pos[0]][_]
            agent_map[now_pos[1]][now_pos[0]][7] = 1
        print("u r dead....start with new agent")
        now_pos = [1,1]
        direction = [1, 0, 0, 0]
        dead = 1
    else:
        for _ in range(7):
            agent_map[now_pos[1]][now_pos[0]][_] = cave_map[now_pos[1]][now_pos[0]][_]
        agent_map[now_pos[1]][now_pos[0]][7] = 1
        dead = 0
    return now_pos, direction, agent_map, dead

# grab the gold
def grab(now_pos):
    # reversed x,y ..... i cant know reason
    print(f"{now_pos[0]}, {now_pos[1]}, {gold_pos}\n{cave_map[now_pos[1]][now_pos[0]]}")
    if (cave_map[now_pos[1]][now_pos[0]][2] == 1):
        cave_map[now_pos[1]][now_pos[0]][2] = 0
        return 1

# shoot arrow
def shoot(now_pos, direction, arrows, cave_map):
    # dirction[E, N, W, S]
    # [Stench, Breeze, Glitter, Bump, Scream, wumpus, pitch]
    # [0, 1, 2, 3, 4, 5, 6]
    print(arrows)
    if(arrows > 0):
        arrows -=1
        print(direction.index(1))
        print(f"remain arrow : {arrows}")
        match int(direction.index(1)):
            case 0:
                # y, x
                print(f"in case 0\n{cave_map[now_pos[1]][now_pos[0] + 1][5]}")
                if cave_map[now_pos[1]][now_pos[0] + 1][5] == 1:
                    cave_map[now_pos[1]][now_pos[0] + 1][5] = 0
                    cave_map[now_pos[1]+ 1][now_pos[0] + 1][0] = 0
                    cave_map[now_pos[1]+ 1][now_pos[0] + 1][4] = 1
                    cave_map[now_pos[1]][now_pos[0] + 1 + 1][0] = 0
                    cave_map[now_pos[1]][now_pos[0] + 1 + 1][4] = 1
                    cave_map[now_pos[1] - 1][now_pos[0] + 1][0] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] + 1][4] = 1
                    cave_map[now_pos[1]][now_pos[0] - 1 + 1][0] = 0
                    cave_map[now_pos[1]][now_pos[0] - 1 + 1][4] = 1
                    #..done
                    # set agent_map
                    agent_map[now_pos[1]][now_pos[0] + 1][5] = 0
                    if agent_map[now_pos[1]+ 1][now_pos[0] + 1][7] == 1:
                        agent_map[now_pos[1]+ 1][now_pos[0] + 1][0] = 0
                        agent_map[now_pos[1]+ 1][now_pos[0] + 1][4] = 1                        
                    if agent_map[now_pos[1]][now_pos[0] + 1 + 1][7] == 1:
                        agent_map[now_pos[1]][now_pos[0] + 1 + 1][0] = 0
                        agent_map[now_pos[1]][now_pos[0] + 1 + 1][4] = 1
                    if agent_map[now_pos[1] - 1][now_pos[0] + 1][7] == 1:
                        agent_map[now_pos[1] - 1][now_pos[0] + 1][0] = 0
                        agent_map[now_pos[1] - 1][now_pos[0] + 1][4] = 1  
                    if agent_map[now_pos[1]][now_pos[0] - 1 + 1][7] == 1:
                        agent_map[now_pos[1]][now_pos[0] - 1 + 1][0] = 0
                        agent_map[now_pos[1]][now_pos[0] - 1 + 1][4] = 1

            case 1:
                # y, x
                print(f"in case 1\n{cave_map[now_pos[1] + 1][now_pos[0]][5]}")
                if cave_map[now_pos[1] + 1][now_pos[0]][5] == 1:
                    cave_map[now_pos[1] + 1][now_pos[0]][5] = 0
                    cave_map[now_pos[1] + 1][now_pos[0] + 1][0] = 0
                    cave_map[now_pos[1] + 1][now_pos[0] + 1][4] = 1
                    cave_map[now_pos[1] + 1 + 1][now_pos[0]][0] = 0
                    cave_map[now_pos[1] + 1 + 1][now_pos[0]][4] = 1
                    cave_map[now_pos[1] + 1][now_pos[0] - 1][0] = 0
                    cave_map[now_pos[1] + 1][now_pos[0] - 1][4] = 1
                    cave_map[now_pos[1] + 1 - 1][now_pos[0]][0] = 0
                    cave_map[now_pos[1] + 1 - 1][now_pos[0]][4] = 1
                    #..done
                    agent_map[now_pos[1] + 1][now_pos[0]][5] = 0
                    if agent_map[now_pos[1] + 1][now_pos[0] + 1][3] != 1:
                        agent_map[now_pos[1] + 1][now_pos[0] + 1][0] = 0
                        agent_map[now_pos[1] + 1][now_pos[0] + 1][4] = 1     
                    if agent_map[now_pos[1] + 1 + 1][now_pos[0]][3] != 1:
                        agent_map[now_pos[1] + 1 + 1][now_pos[0]][0] = 0
                        agent_map[now_pos[1] + 1 + 1][now_pos[0]][4] = 1 
                    if agent_map[now_pos[1] + 1][now_pos[0] - 1][3] != 1:
                        agent_map[now_pos[1] + 1][now_pos[0] - 1][0] = 0
                        agent_map[now_pos[1] + 1][now_pos[0] - 1][4] = 1
                    if agent_map[now_pos[1] + 1 - 1][now_pos[0]][3] != 1:
                        agent_map[now_pos[1] + 1 - 1][now_pos[0]][0] = 0
                        agent_map[now_pos[1] + 1 - 1][now_pos[0]][4] = 1 

            case 2:
                # y, x
                print(f"in case 2\n{cave_map[now_pos[1]][now_pos[0] - 1][5]}")
                if cave_map[now_pos[1]][now_pos[0] - 1][5] == 1: 
                    cave_map[now_pos[1]][now_pos[0] - 1][5] = 0
                    cave_map[now_pos[1]][now_pos[0] - 1 + 1][0] = 0
                    cave_map[now_pos[1]][now_pos[0] - 1 + 1][4] = 1
                    cave_map[now_pos[1] + 1][now_pos[0] - 1][0] = 0
                    cave_map[now_pos[1] + 1][now_pos[0] - 1][4] = 1
                    cave_map[now_pos[1]][now_pos[0] - 1 - 1][0] = 0
                    cave_map[now_pos[1]][now_pos[0] - 1 - 1][4] = 1
                    cave_map[now_pos[1] - 1][now_pos[0] - 1][0] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] - 1][4] = 1

                    agent_map[now_pos[1]][now_pos[0] - 1][5] = 0
                    if agent_map[now_pos[1]][now_pos[0] - 1 + 1][3] != 1:
                        agent_map[now_pos[1]][now_pos[0] - 1 + 1][0] = 0
                        agent_map[now_pos[1]][now_pos[0] - 1 + 1][4] = 1 
                    if agent_map[now_pos[1] + 1][now_pos[0] - 1][3] != 1:
                        agent_map[now_pos[1] + 1][now_pos[0] - 1][0] = 0
                        agent_map[now_pos[1] + 1][now_pos[0] - 1][4] = 1
                    if agent_map[now_pos[1]][now_pos[0] - 1 - 1][3] != 1:
                        agent_map[now_pos[1]][now_pos[0] - 1 - 1][0] = 0
                        agent_map[now_pos[1]][now_pos[0] - 1 - 1][4] = 1    
                    if agent_map[now_pos[1] - 1][now_pos[0] - 1][3] != 1:
                        agent_map[now_pos[1] - 1][now_pos[0] - 1][0] = 0
                        agent_map[now_pos[1] - 1][now_pos[0] - 1][4] = 1   

            case 3:
                # y, x
                print(f"in case 3\n{cave_map[now_pos[1] - 1][now_pos[0]][5]}")
                if cave_map[now_pos[1] - 1][now_pos[0]][5] == 1:
                    cave_map[now_pos[1] - 1][now_pos[0]][5] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] + 1][0] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] + 1][4] = 1
                    cave_map[now_pos[1] - 1 + 1][now_pos[0]][0] = 0
                    cave_map[now_pos[1] - 1 + 1][now_pos[0]][4] = 1
                    cave_map[now_pos[1] - 1][now_pos[0] - 1][0] = 0
                    cave_map[now_pos[1] - 1][now_pos[0] - 1][4] = 1
                    cave_map[now_pos[1] - 1 - 1][now_pos[0]][0] = 0
                    cave_map[now_pos[1] - 1 - 1][now_pos[0]][4] = 1

                    agent_map[now_pos[1] - 1][now_pos[0]][5] = 0
                    if agent_map[now_pos[1] - 1][now_pos[0] + 1][3] != 1:
                        agent_map[now_pos[1] - 1][now_pos[0] + 1][0] = 0
                        agent_map[now_pos[1] - 1][now_pos[0] + 1][4] = 1
                    if agent_map[now_pos[1] - 1 + 1][now_pos[0]][3] != 1:
                        agent_map[now_pos[1] - 1 + 1][now_pos[0]][0] = 0
                        agent_map[now_pos[1] - 1 + 1][now_pos[0]][4] = 1
                    if agent_map[now_pos[1] - 1][now_pos[0] - 1][3] != 1:
                        agent_map[now_pos[1] - 1][now_pos[0] - 1][0] = 0
                        agent_map[now_pos[1] - 1][now_pos[0] - 1][4] = 1
                    if agent_map[now_pos[1] - 1 - 1][now_pos[0]][3] != 1:
                        agent_map[now_pos[1] - 1 - 1][now_pos[0]][0] = 0
                        agent_map[now_pos[1] - 1 - 1][now_pos[0]][4] = 1


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
    
    agent_map[1][1][:7] = cave_map[1][1][:7]
    agent_map[1][1][7] = 1
        
def new_setting():
    now_pos = [1,1]
    # does the agent hold gold
    hold_gold = 0
    # dirction[E, N, W, S]
    direction = [1, 0, 0, 0]
    mk_map()
    global cave_map
    global temp_map
    temp_map = cave_map
    arrows = 2
    for_return = [[1,1]]

    res = {}
    res['cave_map'] = cave_map
    res['for_return'] = for_return
    res['now_pos'] = now_pos
    res['hold_gold'] = hold_gold
    res['direction'] = direction
    res['agent_map'] = agent_map
    res['arrows'] = arrows
    res['act_list'] = []

    return res


#########################################################################
#                    ____  _____ _____ _      _____                     #
#                   /  _ \/  __//  __// \  /|/__ __\                    #
#                   | / \|| |  _|  \  | |\ ||  / \                      #
#                   | |-||| |_//|  /_ | | \||  | |                      #
#                   \_/ \|\____\\____\\_/  \|  \_/                      #
#                                                                       #
#########################################################################

def exec_agent(res):
    now_pos = res['now_pos']
    hold_gold = res['hold_gold']
    direction = res['direction']
    agent_map = res['agent_map']
    arrows = res['arrows']
    act_list = res['act_list']
    for_return = res['for_return']
    cave_map = res['cave_map']

    #################################
    ## 여기에 프론트에서 data 받아옴 ##
    #################################
    # [Stench, Breeze, Glitter, Bump, Scream, wumpus, pitch, visited]
    # [0, 1, 2, 3, 4, 5, 6, 7]
    dead = 0

    if hold_gold == 1:
        if (now_pos == for_return[-1]):
            for_return.pop()
        #dirction[E, N, W, S]
        if(now_pos[0] > for_return[-1][0]):
            if(direction != [0, 0, 1, 0]):
                direction = turn_left(direction)
            else:
                now_pos, direction, agent_map, dead = go_forward(now_pos, direction)
        elif(now_pos[1] > for_return[-1][1]):
            if(direction != [0, 0, 0, 1]):
                direction = turn_right(direction)
            else:
                now_pos, direction, agent_map, dead = go_forward(now_pos, direction)
        elif(now_pos[0] < for_return[-1][0]):
            if(direction != [1, 0, 0, 0]):
                direction = turn_left(direction)
            else:
                now_pos, direction, agent_map, dead = go_forward(now_pos, direction)
        elif(now_pos[1] < for_return[-1][1]):
            if(direction != [0, 1, 0, 0]):
                direction = turn_left(direction)
            else:
                now_pos, direction, agent_map, dead = go_forward(now_pos, direction)

    elif hold_gold != 1:
        if agent_map[now_pos[1]][now_pos[0]][2] == 1:
            hold_gold = grab(now_pos)
            print("hold")

        else:
            match direction.index(1):
                case 0:
                    x = 1
                    y = 0
                case 1:
                    x = 0
                    y = 1
                case 2:
                    x = -1
                    y = 0
                case 3:
                    x = 0
                    y = -1

            if agent_map[now_pos[1]][now_pos[0] + 1][7] == 0 or agent_map[now_pos[1] + 1][now_pos[0]][7] == 0 or agent_map[now_pos[1]][now_pos[0] - 1][7] == 0 or agent_map[now_pos[1] - 1][now_pos[0]][7] == 0:
                match direction.index(1):
                    case 0:
                        print("1")
                        if agent_map[now_pos[1]][now_pos[0] + 1][7] == 0:
                            now_pos, direction, agent_map, dead = go_forward(now_pos, direction)
                        elif agent_map[now_pos[1]][now_pos[0] + 1][5] == 1 and arrows > 0:
                            shoot(now_pos, direction, arrows, cave_map)
                        else:
                            direction = turn_right(direction)
                    case 1:
                        print("2")
                        if agent_map[now_pos[1] + 1][now_pos[0]][7] == 0:
                            now_pos, direction, agent_map, dead= go_forward(now_pos, direction)
                        elif agent_map[now_pos[1] + 1][now_pos[0]][5] == 1 and arrows > 0:
                            shoot(now_pos, direction, arrows, cave_map)
                        else:
                            direction = turn_right(direction)
                    case 2:
                        print("3")
                        if agent_map[now_pos[1]][now_pos[0] - 1][7] == 0:
                            now_pos, direction, agent_map, dead = go_forward(now_pos, direction)
                        elif agent_map[now_pos[1]][now_pos[0] - 1][5] == 1 and arrows > 0:
                            shoot(now_pos, direction, arrows, cave_map)
                        else:
                            direction = turn_right(direction)
                    case 3:
                        print("4")
                        if agent_map[now_pos[1] - 1][now_pos[0]][7] == 0:
                            now_pos, direction, agent_map, dead = go_forward(now_pos, direction)
                        elif agent_map[now_pos[1] - 1][now_pos[0]][5] == 1 and arrows > 0:
                            shoot(now_pos, direction, arrows, cave_map)
                        else:
                            direction = turn_right(direction)
            elif agent_map[now_pos[1] + y][now_pos[0] + x][7] == 1 and agent_map[now_pos[1] + y][now_pos[0] + x][5] == 0 and agent_map[now_pos[1] + y][now_pos[0] + x][6] == 0 and agent_map[now_pos[1] + y][now_pos[0] + x][3] == 0:
                now_pos, direction, agent_map, dead = go_forward(now_pos, direction)
            elif agent_map[now_pos[1]][now_pos[0] + 1][7] == 1 and agent_map[now_pos[1] + 1][now_pos[0]][7] == 1 and agent_map[now_pos[1]][now_pos[0] - 1][7] == 1 and agent_map[now_pos[1] - 1][now_pos[0]][7] == 1:
                match direction.index(1):
                    case 0:
                        print("5")
                        if agent_map[now_pos[1]][now_pos[0] + 1][5] != 1 and agent_map[now_pos[1]][now_pos[0] + 1][6] != 1 and agent_map[now_pos[1]][now_pos[0] + 1][3] != 1:
                            now_pos, direction, agent_map, dead= go_forward(now_pos, direction)
                        elif agent_map[now_pos[1]][now_pos[0] + 1][5] == 1 and arrows > 0:
                            shoot(now_pos, direction, arrows)
                        else:
                            direction = turn_right(direction)
                    case 1:
                        print("6")
                        if agent_map[now_pos[1] + 1][now_pos[0]][5] != 1 and agent_map[now_pos[1] + 1][now_pos[0]][6] != 1 and agent_map[now_pos[1] + 1][now_pos[0]][3] != 1:
                            now_pos, direction, agent_map, dead= go_forward(now_pos, direction)
                        elif agent_map[now_pos[1] + 1][now_pos[0]][5] == 1 and arrows > 0:
                            shoot(now_pos, direction, arrows)
                        else:
                            direction = turn_right(direction)
                    case 2:
                        print("7")
                        if agent_map[now_pos[1]][now_pos[0] - 1][5] != 1 and agent_map[now_pos[1]][now_pos[0] - 1][6] != 1 and agent_map[now_pos[1]][now_pos[0] - 1][3] != 1:
                            now_pos, direction, agent_map, dead= go_forward(now_pos, direction)
                        elif agent_map[now_pos[1]][now_pos[0] - 1][5] == 1 and arrows > 0:
                            shoot(now_pos, direction, arrows)
                        else:
                            direction = turn_right(direction)
                    case 3:
                        print("8")
                        if agent_map[now_pos[1] - 1][now_pos[0]][5] != 1 and agent_map[now_pos[1] - 1][now_pos[0]][6] != 1 and agent_map[now_pos[1] - 1][now_pos[0]][3] != 1:
                            now_pos, direction, agent_map, dead= go_forward(now_pos, direction)
                        elif agent_map[now_pos[1] - 1][now_pos[0]][5] == 1 and arrows > 0:
                            shoot(now_pos, direction, arrows)
                        else:
                            direction = turn_right(direction)



    for j in reversed(range(6)):
        for k in range(6):
            print(agent_map[j][k],end="")
        print()

    print(now_pos)
    print(direction)

    if dead == 1:
        for_return = [[1,1]]
        global cave_map
        global temp_map
        cave_map = temp_map
        for j in range(6):
            for k in range(6):
                if agent_map[j][k][7] == 1:
                    for _ in range(7):
                        agent_map[j][k][_] = cave_map[j][k][_]
    else:
        if for_return[-1] != now_pos and hold_gold == 0:
            for_return.append([now_pos[0], now_pos[1]])

    res['now_pos'] = now_pos
    res['hold_gold'] = hold_gold
    res['direction'] = direction
    res['agent_map'] = agent_map
    res['arrows'] = arrows
    res['act_list'] = act_list
    res['for_return'] = for_return

    return res
    ###############################
    ## 백에서 프론트로 데이터 쏴줌 ##
    ###############################

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
    global now_pos
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
    ###
    res = new_setting()
    ###
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
                go_forward(now_pos, direction)
                print(f"{now_pos}\n{cave_map[now_pos[1]][now_pos[0]]}\n")
            case 5:
                grab(now_pos)
                print(hold_gold)
            case 6:
                shoot(now_pos, direction, arrows)
                print("shoot done")
            case 7:
                for j in reversed(range(6)):
                    for k in range(6):
                        print(agent_map[j][k],end="")
                    print()
            case 8:
                climb()
            case 9:
                res = exec_agent(res)