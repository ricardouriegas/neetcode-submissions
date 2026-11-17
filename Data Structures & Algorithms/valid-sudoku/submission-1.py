class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        sub_boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                current_cell = board[i][j]
                if current_cell == ".":
                    continue
                if current_cell in rows[i] or current_cell in columns[j] or current_cell in sub_boxes[(i // 3, j // 3)]:
                    return False
                
                rows[i].add(current_cell)
                columns[j].add(current_cell)
                sub_boxes[(i // 3, j // 3)].add(current_cell)
                
        return True