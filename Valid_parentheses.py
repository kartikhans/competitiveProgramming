def isValid(s):
        stack=[]
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            elif(i==')'):
                if(len(stack)==0 or stack[-1]!='('):
                    return(False)
                else:
                    stack.pop()
            elif(i=='}'):
                if(len(stack)==0 or stack[-1]!='{'):
                    return(False)
                else:
                    stack.pop()
            else:
                if(len(stack)==0 or stack[-1]!='['):
                    return(False)
                else:
                    stack.pop()
        if(len(stack)==0):
            return(True)
        return(False)