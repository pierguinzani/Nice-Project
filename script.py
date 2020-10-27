no_players = int(input())
candidate_names = []
candidate_heights = []
while(True):
    candiate_name = input()
    if (candiate_name == 'Q' or candiate_name == 'q'):
        break
    candidate_names.append(candiate_name)
while(True):
    candidate_height = float(input())
    if (len(candidate_heights) == len(candidate_names) or (type(candidate_height) != float and type(candidate_height) != int)):
        break
    candidate_heights.append(candidate_height)
max_height = max(candidate_heights)
print(candidate_names[candidate_heights.index(max_height)])