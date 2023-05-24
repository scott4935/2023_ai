import random # for random action e.g.) gold, wumpus, pitch ...



# make map and place gold, wumpus, pitch
def mk_map():
    while(1):
        gold_pos = random.randint(8,28)
        if(7 <= gold_pos <= 10 or 13<= gold_pos <= 16 or 19 <= gold_pos <= 22 or 25 <= gold_pos <= 28):
            break

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
    cave_map = [[[0,0,0,0,0] for col in range(6)]for row in range(6)]
    cave_map[gold_pos // 6][gold_pos % 6][2] = 1

    print(wumpus,end="")
    print(f", {pitch}", end="")
    print(f", {gold_pos}")

    for _ in wumpus:
        print(_)
        cave_map[_ // 6][_ % 6][0] = 1

    for _ in pitch:
        print(_)
        cave_map[_ // 6][_ % 6][0] = 1

    for _ in range(5):
        cave_map[_][0][3] = 1
        cave_map[_][5][3] = 1
    for _ in range(5):
        cave_map[0][_][3] = 1
        cave_map[5][_][3] = 1

    for j in reversed(range(6)):
        for k in range(6):
            print(cave_map[j][k],end="")
        print()
        

# main
if __name__ == "__main__":
	mk_map()