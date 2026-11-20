class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # rows
        for i in range(len(board)):
            c = Counter(board[i])
            for i in c:
                if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and c[i] > 1:
                    return False
        # cols
        for i in range(len(board[0])):
            c = Counter()
            for j in board:
                if j[i] not in c:
                    c[j[i]] = 1
                else:
                    c[j[i]] += 1
            for k in c:
                if k in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and c[k] > 1:
                    return False
        # sub-boxes
        m = 0
        for i in range(0, 3):
            n = 0
            for j in range(0, 3):
                c = Counter()
                for a in range(m, m + 3):
                    for b in range(n, n + 3):
                        if board[a][b] not in c:
                            c[board[a][b]] = 1
                        else:
                            c[board[a][b]] += 1
                for k in c:
                    if k in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and c[k] > 1:
                        return False
                n += 3
            m += 3
        return True