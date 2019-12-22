def factRecursif(a):
    assert a >= 0, 'value should be positive'
    if a == 0:
        return 1
    else:
        if a > 0:
            return a*factRecursif(a-1)
        
def factIteratif(a):
    assert a >= 0, 'value should be positive'
    if a == 0:
        return 1
    else:
        i = a
        while(i > 1):
            i -= 1
            a *= i
        return a
    
#start test factorielle 
factRecursif(3) #--> 6
factIteratif(3) #--> 6
factRecursif(0) #--> 1
factIteratif(0) #--> 1
#end test section secondDegree  

 
    
       


            
        
    