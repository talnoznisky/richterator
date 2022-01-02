from random import randint
import math
class Matrix:
    def __init__(self,
                 charset='#',
                 mode='block',                 
                 columns=4,
                 rows=4,
                 block_width=24,
                 block_height=None
                ):
        self.charset        = charset
        self.mode           = mode
        self.columns        = int(columns)
        self.rows           = int(rows)
        self.block_width    = int(block_width)
        self.block_height   = int(math.ceil(block_width/2)) if not block_height else block_height
        self.matrix_chars   = self.generate_char_list()


    def generate_color_dict(self, num):
        return {f'color_{i}': randint(50,250) for i in range(num)}


    def generate_char_list(self):
        total_char = self.block_width * self.block_height
        return [self.charset[randint(0,len(self.charset)-1)] for _ in range(total_char)]


    def generate_matrix(self):
        rows        = self.rows
        cols        = self.columns
        b_height    = self.block_height
        b_width     = self.block_width

        mode = self.mode
        
        matrix_chars = self.matrix_chars
        matrix = ''

        
        
        for rows in range(rows):    
            start = 0
            row = ''
            colors = self.generate_color_dict(cols)
            
            for b_row in range(b_height):    
                outerline = ''
                
                for col in range(cols):
                    innerline = ''
                
                    for b_col in range(b_width):
                        char_sub = matrix_chars[start:start+b_width]
                        color = colors[f'color_{col}'] \
                            if mode == 'block' else randint(1,257)
                        char = char_sub[b_col]
                        innerline += f"\033[48m\033[38;5;{color}m{char}\033[0m"
                
                    outerline += f'{innerline}   '
                
                
                row += outerline + '\n'
                start = start + b_width
            matrix += row + '\n'

        return matrix

m = Matrix()
m.generate_matrix()