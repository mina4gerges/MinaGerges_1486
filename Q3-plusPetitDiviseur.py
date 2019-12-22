from math import sqrt
def plusPetitDiviseur(n):
    '''
    tester tous les nombre n entre 1 et radical de N
    pour voir si le rest de la division de N par n 
    est egale a
    
    plus petit diviseur est le nombre > 1
    
    si apres le test il n'y pas autre que 1 comme un diviseur --> le nombre lui
    meme est le plus petit diviseur
    '''
    assert n > 0 ,'nombre doit etre positive'
    finalRes = 0
    nbrRange = int(sqrt(n))
    for x in range(nbrRange):
        tempRes = n % (x+1)
        if(tempRes == 0):
            finalRes = (x+1)
    if(finalRes == 1):
        finalRes = n
    return finalRes
        
#start test plusPetitDiviseur
plusPetitDiviseur(6)  # --> 2    
plusPetitDiviseur(35) # --> 5
#end test section plusPetitDiviseur  

