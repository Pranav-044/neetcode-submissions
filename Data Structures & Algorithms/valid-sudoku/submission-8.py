from itertools import chain
def check_row(row):
        dictionary={}
        for j in set(row):
            dictionary[j]=0
        
        for i in row:
            if(i!="."):
                dictionary[i]+=1
                if dictionary[i]>1:
                    return False
        return True    
def check_col(col_no,board):
        col=[nums[col_no] for nums in board]
        dictionary={}
        for j in set(col):
            dictionary[j]=0
        
        for i in col:
            if(i!="."):
                dictionary[i]+=1
                if dictionary[i]>1:
                    return False
        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            square_final=True
            row_final=check_row(board[i])
            col_final=check_col(i,board)
            if((i+1)%3 == 0):
                number=i
                row1=[row[number-2:number+1] for row in board[number-2:number+1]]
                row2=[row[number+1:number+4] for row in board[number-2:number+1]]
                row3=[row[number+4:number+7] for row  in board[number-2:number+1]]
                sq1 = list(chain.from_iterable(row1))
                sq2 = list(chain.from_iterable(row2))
                sq3 = list(chain.from_iterable(row3))
                square_final=check_row(sq1) and check_row(sq2) and check_row(sq3)
            result=row_final and col_final and square_final
            if not result:
                return False
        return True

            


  
        

