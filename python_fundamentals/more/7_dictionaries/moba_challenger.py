data = input()
players_pool = {}
sum_skill = {}
while data != "Season end":

    if "->" in data:
        player, position, skill = data.split(" -> ")

        if player not in players_pool:
            players_pool[player] = {}
            players_pool[player][position] = int(skill)

        else:
            for key, values in players_pool[player].items():
                if values < int(skill):
                    players_pool[player][position] = int(skill)
                    break

    else:
        data_split = data.split(" ")
        player1 = data_split[0]
        player2 = data_split[2]
        if player1 in players_pool and player2 in players_pool:
            for key in players_pool[player1].keys():
                if key in players_pool[player2].keys():
                    sum1 = sum(players_pool[player1].values())
                    sum2 = sum(players_pool[player2].values())
                    if sum1 > sum2:
                        del players_pool[player2]
                    elif sum2 < sum1:
                        del players_pool[player1]

    data = input()

for player in players_pool.keys():
    total_skills = sum(players_pool[player].values())
    sum_skill[player] = str(total_skills)

for player, skill in sorted(sum_skill.items(), reverse=True, key=lambda x: x[1]):
    print(f"{player}: {skill} skill")
    for key, value in sorted(players_pool[player].items(), reverse=True, key=lambda x: x[1]):
        print(f"- {key} <::> {value}")
