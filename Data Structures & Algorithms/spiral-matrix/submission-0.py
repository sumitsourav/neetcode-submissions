class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        no_of_elements = rows * cols
        seen = {}
        res = []
        current_dir = 0
        r, c = 0, 0
        while no_of_elements > len(res):
            res.append(matrix[r][c])
            seen[(r,c)] = True
            cr, cc = directions[current_dir]
            next_r, next_c = r + cr, c + cc
            if 0 <= next_r < rows and 0 <= next_c < cols and (next_r, next_c) not in seen:
                r, c = next_r, next_c
            else:
                current_dir = (current_dir + 1) % 4
                dr, dc = directions[current_dir]
                r, c = r + dr, c + dc
        return res



            


        