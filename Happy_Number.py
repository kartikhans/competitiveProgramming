def isHappy(n):
            kappa=str(n)
            sume=0
            while(sume!=4 and sume!=1):
                sume=0
                for i in kappa:
                    sume+=int(i)**2
                kappa=str(sume)
            if(sume==1):
                return(True)
            return(False)

print(isHappy(3))