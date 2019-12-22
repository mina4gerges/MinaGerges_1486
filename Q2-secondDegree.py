from math import sqrt
def secondDegree(a,b,c):
    '''    
    ax^2+bx+c=0
    if a == 0 --> equation du premier degre
    calcule du discriminant
    Δ = b² - 4ac
    
    Si Δ < 0 --> pas de solution.
    Si Δ = 0 --> x = -b/(2a)
    Si Δ > 0 --> x1 = (-b-√Δ)/(2a) et x2= (-b+√Δ)/(2a)
    '''
    finalRes = None
    if a == 0:
        #equation premier degree 
        finalRes = 'Solution du premier degree',pgmPremDegre(b,c)
    else:
        discriminant = b*b - 4*a*c
        
        if discriminant < 0:
            finalRes = 'Pas de solution'
        elif discriminant == 0:
            finalRes = 'Une solution :',-(b/(2*a))
        else:
            sol1 = (-b -sqrt(discriminant)) / (2*a)
            sol2 = (-b +sqrt(discriminant)) / (2*a)
            finalRes = 'Solution 1 :',sol1,'Solution 2 :',sol2
    return finalRes

def pgmPremDegre(a,b):
    '''
    print("saisir a et b pour calculer ax+b=0")
    x=int(input("Donner a "))
    y=int(input("Donner b "))
    '''
    rep=premDegre(a,b)
    #print("la solution de",x,"x +",y,"= 0 est ",rep)
    return rep
    
def premDegre(a,b):
    # assert permet de faire de la programation deffensive
    assert a!=0 ,'A ne doit pas être nul'
    return -b/a

#start test section secondDegree
secondDegree(0,4,1) #--> Solution du premier degree (-0.25)
secondDegree(1,1,-2) #--> deux solution (-2;1)
secondDegree(1,1,1) #--> pas de solution
secondDegree(4,4,1) #--> une solution (-0.5)
#end test section secondDegree  