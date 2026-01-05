import numpy as np
def teacherSolution():
    #generate the array 3x10 random
    array=np.random.random((3,10))*10+10
    print(array)
    print(abs(array-15))
    #identify the nearest balue of 15 on each of the lines

    #find the position (indice) of the nearest on the array
    indice = abs(array-15).argmin(axis=1)
    print(indice)

    #print the nearest value of 15 on each of the lines
    print(array[(0,1,2),indice])

#my solution
def mySolution():
    array=np.random.uniform(10,20,size=(3,10))
    print(array)


mySolution()

