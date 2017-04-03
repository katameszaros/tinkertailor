
def tinker(count, player_num):
    players = list(range(1, player_num+1))
    prev = 0
    index = 0
    while len(players)>1:
        print(players)
        index = (prev+count-1) % len(players)
        players.remove(players[index])
        prev = index
    print(players)

tinker(3,5)

