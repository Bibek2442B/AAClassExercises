# set consisting of n1 elements of a certain data type and n2 of other datatyoe
#Exercise 02

from math import log2

#entropy function
def entropy(number1, number2):
    if number1<0 or number2<0:
        return ('Invalid quatities!!!')
    elif number1==0 or number2==0:
        return 0
    else:
        #p1=n1/(n1+n2)
        p1 = number1/(number1+number2)
        #p2=n2/(n1+n2)
        p2=number2/(number1+number2)

        #Entropy
        entropy = -p1*log2(p1) -p2*log2(p2)
        return entropy
    return 0

def entropyN(*quantities):
    sumAll=0
    totalItems=sum(quantities)
    if totalItems==0:
        print('Empty set!!!')
        return 0
    for n in quantities:
        if n<0:
            print('Invalid quatities!!!')
            return None
        elif n>0:
            p = n/totalItems

        sumAll+=-p*log2(p)
    return sumAll
#main code
#p1=n1/(n1+n2) and p2=n2/(n1+n2)
n1=20
n2=20

print('{0:.2f}:entropy of a set within {1} elements of a 1st ' \
      'type and {2} elements of a 2nd type.'.format(entropy(n1,n2), n1,n2))

n1=20
n2=180

print('{0:.2f}:entropy of a set within {1} elements of a 1st ' \
      'type and {2} elements of a 2nd type.'.format(entropy(n1,n2), n1,n2))

n1=100
n2=20

print('{0:.2f}:entropy of a set within {1} elements of a 1st ' \
      'type and {2} elements of a 2nd type.'.format(entropyN(n1,n2), n1,n2))