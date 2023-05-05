#!/usr/bin/env python3

def is_valid_sodok(grid):
    rows = [{} for _ in range(len(grid))]
    cols = [{} for _ in range(len(grid))]
    grids = [{} for _ in range(len(grid))]

    for ri, row in enumerate(grid):
        for ci, num in enumerate(row):
            if num == '.':
                continue
            grid_index = (ri // 3) * 3 + (ci // 3)
            if num in rows[ri] or num in cols[ci] or num in grids[grid_index]:
                return False
            rows[ri][num] = 1
            cols[ci][num] = 1
            grids[grid_index][num] = 1
    return True
   
    # rows = [set() for _ in range(9)]
    # column = [set() for _ in range(9)]
    # sub_boxes = [set() for _ in range(9)]

    # for i in range(9):
    #     for j in range(9):
    #         if grid[i][j] ==".":
    #             continue

    #         num = int(grid[i][j])

    #         sub_boxes_index = (i // 3) * 3 + j // 3
            
    #         if num in rows[i] or num in column[j] or num in sub_boxes[sub_boxes_index]:
    #             return False

    #         rows[i].add(num)
    #         column[j].add(num)
    #         sub_boxes[sub_boxes_index].add(num)

    # return True



# from typing import List


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         row_dict = {}
#         col_dict = {}
#         grid_dict = {}
#         for row_index, row in enumerate(board):
#             for col_index, col in enumerate(row):
#                 print(row_index, col_index, col)








board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(is_valid_sodok(board))
# sol = Solution()
# sol.isValidSudoku(board)