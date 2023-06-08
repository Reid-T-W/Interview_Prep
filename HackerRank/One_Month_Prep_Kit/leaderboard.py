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
    # dict and list to store rankings
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
        if player[player_index] >= ranked[ranked_index]:
            rankings[player[player_index]] = ranked_index + 1
            player_index += 1
        else:
            ranked_index += 1
    if player_index < len(player):
        remaining = len(player) - (player_index)
        for i in range(remaining):
            rankings[player[player_index + i]] = ranked_index + 1
            print(rankings)
            
    # Required so that duplicate players can have the same rank
    for rank in backup_player:
        rankings_list.append(rankings[rank])
    return rankings_list

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
