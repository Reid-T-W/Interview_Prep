#!/bin/python3
from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        queue = deque()
        queue.appendleft((sr, sc))
        prev_color = image[sr][sc]

        while queue:
            position = queue.popleft()
            if position in visited:
                continue
            
            visited.add(position)
            
            # Change the color
            sr = position[0]
            sc = position[1]
            image[sr][sc] = color

            # Register all neighbours with the same color
            if sr + 1 < len(image) and image[sr + 1][sc] == prev_color:
                queue.appendleft((sr + 1, sc))
            if sr - 1 >= 0 and image[sr - 1][sc] == prev_color:
                queue.appendleft((sr - 1, sc))
            if sc + 1 < len(image[0]) and image[sr][sc + 1] == prev_color:
                queue.appendleft((sr, sc + 1))
            if sc - 1 >= 0 and image[sr][sc - 1] == prev_color:
                queue.appendleft((sr, sc - 1))
        return(image)

sol = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
sol.floodFill(image, sr, sc, color)


# [
#   [2 2 2],
#   [2 2 0],
#   [2 0 1],
# ]

# queue = []
# visited = {(1, 1), (0, 1), (1, 0), (0, 0), (0, 2)}

# color_to_look_for = 1
# visited = [(1, 1), (0, 1), (1, 0), (0, 0), (0, 2), (2, 0)]