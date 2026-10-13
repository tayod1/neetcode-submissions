class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        # use double for loop to traverse array
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # compute bit val
                val = int(board[r][c]) - 1

                # left-shift bit 'val' times
                mask = 1 << val
                # apply a unique mask to handle duplicate nums 
                
                # check if already seen
                if mask & rows[r]:
                    return False
                if mask & cols[c]:
                    return False
                if mask & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                
                # mark as seen
                rows[r] |= mask
                cols[c] |= mask

                # r // 3: Tells us which "row" of boxes we are in (0, 1, or 2)
                # * 3: Shifts that row index to the start of the box sequence (0, 3, or 6)
                squares[(r // 3) * 3 + (c // 3)] |= mask
                # c // 3: Tells us which "column" of boxes we are in (0, 1, or 2)

        return True
        