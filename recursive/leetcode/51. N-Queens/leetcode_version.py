class Solution:
    def solveNQueens(self, n):
        def could_place(row, col):
            print("       Call could_place :  row : ",  row , " - col : ", col)
            is_could_pplace = (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
            print("       Calculate is_could_place :", is_could_pplace)
            return not is_could_pplace
        
        def place_queen(row, col):
            print("          Call place_queen. put row : ", row, " - col : ", col )
            queens.add((row, col))
            print("          queens : ", queens)

            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
            print("              cols : ", cols,  " - hill_diagonals : ", hill_diagonals , " - dale_diagonals : ", dale_diagonals)
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
        
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtrack(row = 0):
            print("   row : ", row)
            for col in range(n):
                print("   col : ", col)
                is_could_place =  could_place(row, col)
                print("   return is_could_place : ", is_could_place)
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)
        
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        print('cols : ', cols)
        print('hill_diagonals : ', hill_diagonals)
        print('dale_diagonals : ', dale_diagonals)
        queens = set()
        print('queens : ', queens)

        output = []
        backtrack()
        return output


res = Solution().solveNQueens(4)
print("res : ", res)