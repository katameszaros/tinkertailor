
def tinker(count, player_num):
    players = list(range(1, player_num+1))
    previous_index = 0
    result = []
    while len(players)>0:
        index = (previous_index + count - 1) % len(players)
        result.append(players[index])
        players.remove(players[index])
        previous_index = index
    return result


def main():
    print(tinker(count=3, player_num=5))

main()

