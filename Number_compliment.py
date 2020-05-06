def findComplement(num):
        kaim=bin(num)[2:]
        sup=""
        for i in kaim:
            if(i=='0'):
                sup+='1'
            else:
                sup+='0'
        return(int(sup,2))