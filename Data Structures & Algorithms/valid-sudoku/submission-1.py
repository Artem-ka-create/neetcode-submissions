class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_seen = defaultdict(set)
        row_seen = defaultdict(set)
        box_seen = defaultdict(set)


        for col in range(0,len(board)):    
            for row in range(0,len(board)):
                if (board[col][row]=="."):continue

                if board[col][row] in col_seen[col] or board[col][row] in row_seen[row] or board[col][row] in box_seen[(col//3,row//3)]:
                    return False

                col_seen[col].add(board[col][row])
                row_seen[row].add(board[col][row])
                box_seen[(col//3,row//3)].add(board[col][row])

        return True





