import sys
import time
import inputPuzzle
import DomainConstraints
from AC3_Backtracking import *

#importing required variables
rows = inputPuzzle.rows
columns = inputPuzzle.columns
HorizontalMat = inputPuzzle.HorizontalMat
VertMat = inputPuzzle.VertMat

constraint_matrix = DomainConstraints.constraint_matrix
varDict = DomainConstraints.varDict
constraintVar_dict = DomainConstraints.constraintVar_dict
constraintVar_num = DomainConstraints.constraintVar_num



# Calculating time for arc consistency and regular back tracking search
start = time.time()    

arcList = [] 
# Creating arcLists
for i in range( 1 , constraintVar_num + 1 ) :
    for j in constraintVar_dict[i]['neighbours'] :
        arcList.append( (j , i) )
        arcList.append( (i , j) )


# Calling AC3 function 
AC3(arcList)


# Calling backtracking search
Recursive_Backtracking()

end = time.time()           # ending time 
print( "time" , end - start)        # printing time 
print("\n")

printMetrics()


# # Outputting to a text file

outputFile = open(sys.argv[2], 'w')

    #writing first three lines same as input text file 
outputFile = open(sys.argv[2], 'w')

    #writing first three lines same as input text file 
RowsLine = "rows=" + str(rows) + "\n"
ColumnsLine = "columns=" + str(columns) + "\n"

outputFile.write(RowsLine)
outputFile.write(ColumnsLine)
outputFile.write("Horizontal\n")

    # Changing values of unassigned variables in horizontal and vertical matrices from assignment 
for var in varDict.keys():
    HorizontalMat[var[0]][var[1]] = assignmentList[-1][var]
    VertMat[var[0]][var[1]] = assignmentList[-1][var]

    # wrting horizontal matrix
for row in range(rows):
    for col in range(columns):
        if(col == 0):
            outputFile.write(str(HorizontalMat[row][col]))
        else:
            outputFile.write(","+ str(HorizontalMat[row][col]))
    outputFile.write("\n")

    # writing vertical matrix
outputFile.write("Vertical\n")
for row in range(rows):
    for col in range(columns):
        if(col == 0):
            outputFile.write(str(VertMat[row][col]))
        else:
            outputFile.write(","+ str(VertMat[row][col]))
    outputFile.write("\n")
