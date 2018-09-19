import numpy as np

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board = np.array(board)

        for i in range(0, 9):
            if False == judge(board[i]):
                return False

        for i in range(0, 9):
            if False == judge(board[:,i]):
                return False


        for i in range(0, 3):
            for j in range(0, 3):
                row_begin = i * 3
                row_end = row_begin + 3
                col_begin = j * 3
                col_end = col_begin + 3
                if False == judge(board[row_begin:row_end, col_begin:col_end].flatten()):
                    return False

        return True

def judge(arr):
    origin_dict = {}
    for j in ''.join(arr).replace('.', ''):
        if origin_dict.has_key(j):
            return False
        else:
            origin_dict[j] = True
    return True
