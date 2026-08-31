class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=-1
        s_set=set(["}","]",")"])
        if(s == ""):
            return True
        elif(len(s)==1):
            return False
        while i<(len(s)-1):
            i+=1
            if(s[i] not in s_set):
                stack.append(s[i])
                
            else:
                if(not len(stack)):
                    return False
                else:

                    if(stack !=[] and s[i] == "}"):
                        if(stack[-1] == "{"):
                            stack.pop()
                            
                        else:
                            return False 
                    if(stack !=[] and s[i] == ")"):
                        if(stack[-1] == "("):
                            stack.pop()
                        
                        else:
                            return False 
                    if(stack !=[] and s[i] == "]"):
                        if(stack[-1] == "["):
                            stack.pop()
                        
                        else:
                            return False 
        else:
            if(stack == []):
                return True
            else:
                return False
                    
                

        