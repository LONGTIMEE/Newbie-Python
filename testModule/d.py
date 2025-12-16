import numpy as np

def calScore(x):
    a = np.sum(x)
    if x >79 :
        return ("A")
    elif x>=70 :
        return("B")
    elif x>=60 :
        return("C")  
    elif x>=50 :
        return("D")
    else :
        return("อ่อนมากกกกกก") 
    