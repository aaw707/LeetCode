class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        if len(moves) < 5:
            return "Pending"
        
        # put moves into matrix
        matrix = [['' for i in range(3)] for j in range(3)]
        for i in range(len(moves)):
            if i % 2 == 0:
                matrix[moves[i][0]][moves[i][1]] = 'A'
            else:
                matrix[moves[i][0]][moves[i][1]] = 'B'
        
        # check the rows
        for row in matrix:
            if row[0] == row[1] == row[2]:
                if row[0] == 'A':
                    return 'A'
                elif row[0] == 'B':
                    return 'B'
           
        # check the cols
        for col in range(3):
            if matrix[0][col] == matrix[1][col] == matrix[2][col]:
                if matrix[0][col] == 'A':
                    return 'A'
                elif matrix[0][col] == 'B':
                    return 'B'
        
        # check diagonals
        if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
            if matrix[1][1] == 'A':
                return 'A'
            elif matrix[1][1] == 'B':
                return 'B'
        
        # no winner yet
        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"
             