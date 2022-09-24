class Sudoku(object):
    def __init__(self, data):
        self.data = data
        
    def is_valid(self):
        
        grid = len(self.data[0])
        
        if len(self.data) == 1:
            if isinstance(self.data[0], list):
                if (
                    len(self.data[0]) == 1 
                    and type(self.data[0][0]) == int
                    and self.data[0][0] == 1
                    ):
                        print(self.data[0][0])
                        return True
                return False
            elif isinstance(self.data[0], int):
                if self.data[0][0] == grid:
                    return True
                return False
            else:
                return False
        
        for row in self.data:
            for num in row:
                if not num in range(1, grid + 1) and not isinstance(num, int):
                    return False
            if len(set(row)) != grid:
                return False
        
        index = 0
        row = 0
        column = []
        
        while index < len(self.data):
            while row < len(self.data):
                if self.data[row][index] in range(1, grid + 1) and isinstance(self.data[row][index], int):
                    column.append(self.data[row][index])
                    row += 1
                else:
                    return False
            if len(set(column)) != grid:
                return False
            index += 1
            row = 0
            column = []
        

        index = 0
        piece = 0
        step = int(grid**0.5)
        stop = step
        little_squares = []
        
        while index < len(self.data):
            if stop < len(self.data):
                little_squares.extend(self.data[index][piece:stop])
            else:
                little_squares.extend(self.data[index][piece:])
            if len(little_squares) == grid:
                if len(set(little_squares)) != grid:
                    return False
                little_squares = []
            index += 1
            if index == len(self.data):
                piece += step
                stop += step
                if piece < len(self.data):
                    index = 0

        return True

                




sudoku = [
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],
  
  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],
  
  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

sudo_bool = zip(*sudoku)
my_obj_sudoku = Sudoku(sudo_bool)
