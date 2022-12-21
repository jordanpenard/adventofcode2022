

f = open("input_day02.txt", "r")

input_data = [x.split(" ") for x in f.read().split("\n") if x]

opponent_map = {"A":"Rock", "B":"Paper", "C":"Scisor"}
me_map = {"X":"Rock", "Y":"Paper", "Z":"Scisor"}

games = [(opponent_map[x[0]],me_map[x[1]]) for x in input_data]

shape_score = {"Rock":1, "Paper":2, "Scisor":3}
result_score = {"Win":6, "Draw":3, "Lost":0}

me_win_condition = {"Rock":"Paper", "Paper":"Scisor", "Scisor":"Rock"}

def game_result(opponent_shape, me_shape):
    if (opponent_shape == me_shape):
        return "Draw"
    elif (me_win_condition[opponent_shape] == me_shape):
        return "Win"
    else:
        return "Lost"

results_per_match = [result_score[game_result(opponent_shape, me_shape)]+shape_score[me_shape] for (opponent_shape, me_shape) in games]

print("Part 1 : " + str(sum(results_per_match)))

outcome_map = {"X":"Lost", "Y":"Draw", "Z":"Win"}

def required_shape(opponent_shape, outcome):
    if (outcome == "Draw"):
        return opponent_shape
    elif (outcome == "Win"):
        return me_win_condition[opponent_shape]
    else:
        return [k for k, v in me_win_condition.items() if v == opponent_shape][0]

games_part2 = [(opponent_map[x[0]],outcome_map[x[1]]) for x in input_data]
outcome_resolved = [(opponent_shape, required_shape(opponent_shape, outcome)) for (opponent_shape, outcome) in games_part2]

results_per_match_part2 = [result_score[game_result(opponent_shape, me_shape)]+shape_score[me_shape] for (opponent_shape, me_shape) in outcome_resolved]

print("Part 2 : " + str(sum(results_per_match_part2)))
