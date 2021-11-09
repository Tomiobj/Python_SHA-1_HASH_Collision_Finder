from datetime import datetime
from itertools import count
import random
def fun1(strng):
    transformedString = ""
    second = 0
    for each in range(0, len(strng)):
        #second = int(datetime.now().strftime("%S")) + random.randint(40,200)
        #transformedString+= transformedString  + str(ord(strng[each])) #ascii value of each character
        second = second + ord(strng[each])
    transformedString = str(second)
    #return str(int(transformedString)*second)[0 : 40] 
    return str(int(transformedString)*random.randint(40,200)**random.randint(100,150))[0 : 80] #80 higher order bit

def fun2():
    intermediates = {
        "string1" : "Hello1",
        "string2" : "Hello2"
    }
    x1= intermediates["string1"]
    x2= intermediates["string2"]
    k=1 
    while intermediates["string1"] is not intermediates["string2"]: #turtle
        print("-------------------------------\n")
        print("x1 - ", x1, ", x2 - ", x2)
        print("k -", k,)
        intermediates["string1"] = fun1(intermediates["string1"]) 
        i=0
        while i<2: #hare
            intermediates["string2"] = fun1(intermediates["string2"]) 
            if intermediates["string1"] == intermediates["string2"]:
                print("hash1 - ", intermediates["string1"])
                print("hash2 - ", intermediates["string2"])
                return(x1, x2, k) #return statemet
            i=i+1
        k=k+1


print(fun2())