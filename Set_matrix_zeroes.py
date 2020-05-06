def setZeroes(matrix):
        xaxis={}
        yaxis={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    if i not in xaxis:
                        xaxis[i]=1
                    if j not in yaxis:
                        yaxis[j]=1
        for i in xaxis:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in yaxis:
            for j in range(len(matrix)):
                matrix[j][i]=0