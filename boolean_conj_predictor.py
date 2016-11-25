
import numpy as np

TUPLE_FAIL = 100
TUPLE_SUCCESS = 101

def parseFile(filePath) :
    x  = []
    y = []
    training_examples = np.loadtxt(filePath)

    for line in training_examples :
        x.append(line[:-1])
        y.append(line[-1:])

    return x,y

# h is two dimentional array with two cells in each row.
# the number of rows is the number of variabels (x1,x2,x3,..)
# the first column is flag for xi and the second column is flag for not(xi)
# if the flag is 1 - the variable exist, of 0 - its not exist
def calcTupleOnHypothesis(tuple, h):
    for i, item in enumerate(tuple):
        if((h[i][0] == 1 and item==0) or
            (h[i][1] == 1 and item == 1)):
            return TUPLE_FAIL
    return TUPLE_SUCCESS

def algorithm(x,y) :
    h = []
    for i in range(len(x[0])):
        h.append([1,1])

    for index , tuple in enumerate(x) :
        if(y[index] == 1 and calcTupleOnHypothesis(tuple,h) == TUPLE_FAIL):
            for index, item in enumerate(tuple):
                if item==1:
                    h[index][1] = 0
                else:
                    h[index][0] = 0
    return h


if __name__ == '__main__':
    x , y = parseFile("D:\Code\MachineLearning\ex1\example1.txt")
    h = algorithm(x,y)

    outputFile = open("D:\Code\MachineLearning\ex1\output.txt", "w+")

    for index , item in enumerate(h):
        if item[0] == 1 :
            outputFile.write("x"+str(index+1)+",")
        elif item[1] == 1:
            outputFile.write("not(x" + str(index+1)+"),")
