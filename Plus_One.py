def plusOne(nums):
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]==9):
                digits[i]=0
            else:
                digits[i]+=1
                return(digits)
        cop=[1]
        for i in range(len(digits)):
            cop.append(0)
        return(cop)