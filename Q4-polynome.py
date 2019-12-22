#Calculer p(x)=a0+a1*x+..+ai*xi+...+an*xn
def calcPolynome(list):
    a = list[0]
    b = 0
    for key,i in enumerate(list):
        if(key!=0):#skip first element bcz it is a
            b += i
    return pgmPremDegre(a,b)

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
    
#start test calculePolynome
calcPolynome([1,2,3,4,5]) #--> -14 (a0: 1/a1: 2/a3: 3/a4:4 a5: 5)
calcPolynome([2,2,3,4,5]) #--> -7.0
calcPolynome([0,2,3,4,5]) #error la premier valeur ne doit pas etre 0
#end test section calculePolynome 

