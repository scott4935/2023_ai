import random # for random action e.g.) gold, wumpus, pitch ...



# make map and place gold, wumpus, pitch
def mk_map():
    gold_pos = random.randint(2,16)
    while True:
        wumpus = []
        pitch = []
        for i in range(1,16):
            if i == gold_pos:
                continue
            rand_val = random.randrange(100)
            if rand_val < 10:
                wumpus.append(i)
                continue
            elif rand_val < 20:
                pitch.append(i)
        if (len(wumpus) != 0) and (len(pitch) != 0):
            break
    cave_map = [[0,0,0,0,0] for col in range(16)]
    cave_map[0][2] = 1
    print(wumpus)
    print(pitch)
    print(gold_pos)
    print(cave_map)


# main
if __name__ == "__main__":
	mk_map()