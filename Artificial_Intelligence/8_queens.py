class Board:
    def __init__(self):
        self.board = []


    def make_board(self):
        for row in range(8):
            rows = []
            for col in range(8):
                cell = Cell(row, col)
                rows.append(cell)
            self.board.append(rows)


    def queens(self):
        print("Enter the positions of the queens: ")
        for i in range(8):
            queen_row = int(input(f"{i}-th Queen's Column is: {i} and Row is: "))
            self.board[queen_row][i].has_queen = True

                    
    def attacking_queens(self):
        attacking_queens = set()
        
        for row in self.board:
            for cell in row:
                for other_cell in row:
                    if cell != other_cell and cell.has_queen and other_cell.has_queen:
                        if cell.is_attacking(other_cell):
                            attacking_queens.add(cell)
                            
        return attacking_queens if len(attacking_queens) > 0 else None
        
    

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_queen = False


    def is_attacking(self, other):
        # row same
        is_row_same = self.x == other.x

        # diagonal
        is_diagonal = self.x - other.x == self.y - other.y
        
        return is_row_same or is_diagonal

        
    def __repr__(self):
        q = 'Q' if self.has_queen else 'E'
        return q



b = Board()
b.make_board()
b.queens()
for c in b.attacking_queens():
    print(c.x, c.y)



