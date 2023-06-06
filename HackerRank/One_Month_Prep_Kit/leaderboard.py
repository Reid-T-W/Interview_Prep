#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here

    # convert ranked to a set while maintaining order
    set_ranked = dict.fromkeys(ranked)
    ranked = list(set_ranked.keys())


    # convert player to a set while maintaining order
    backup_player = player
    set_player = dict.fromkeys(player)
    player = list(set_player.keys())

    # dict to store rankings
    rankings = {}
    rankings_list = []
    # Populate rankings
    rankings = dict.fromkeys(player)

    # Sort player in deserding order
    player.sort(reverse=True)

    # Pointer to first element in ranked
    ranked_index = 0
    # Pointer to first element in player
    player_index = 0

    # Loop through ranked
    while ranked_index < len(ranked) and player_index < len(player):
        # print( player_index, ranked_index)
        # print( player[player_index], ranked[ranked_index])
        if player[player_index] >= ranked[ranked_index]:
            rankings[player[player_index]] = ranked_index + 1
            # rankings.append(ranked_index + 1)
            player_index += 1
        else:
            ranked_index += 1
    if player_index < len(player):
        remaining = len(player) - (player_index)
        for i in range(remaining):
            rankings[player[player_index + i]] = ranked_index + 1
            # rankings.append(ranked_index + 1)
    
    for rank in backup_player:
        rankings_list.append(rankings[rank])
    return rankings_list
    # return list(rankings.values())

    # # Perform binary search on ranked to find the index of player's score
    # rankings = []
    # dic = {}
    # set_ranked = dic.fromkeys(ranked)
    # ranked = list(set_ranked.keys())
    # print(ranked)
    # for score in player:
    #     first = 0
    #     second = len(ranked) - 1

    #     # Edge Cases
    #     if score >= ranked[first]:
    #         rankings.append(0 + 1)
    #         continue
    #     elif score <= ranked[second]:
    #         rankings.append(len(ranked))
    #         continue

    #     while first + 1 != second:
    #         # print(first, second)
    #         half = (first + second) // 2
    #         if score <= ranked[half]:
    #             first = half
    #         elif score >= ranked[half]:
    #             second = half
    #     rankings.append(first + 1)
    # print(rankings)
    # return rankings    


# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
