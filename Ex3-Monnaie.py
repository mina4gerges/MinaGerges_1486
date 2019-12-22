# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 11:57:24 2019

@author: mina2
"""

class Monnaie:
    
    def __init__(self):
        self.valeur = 0
        self.devise = None
        
    def clearMonnaie(self):
        self.valeur = 0
        self.devise = None
    
    def ajouterMonnaie(self,monnaieAjouter, devise):
        try:
            newMonnaie = self.ajouteDeuxNbr(self.valeur,monnaieAjouter)
            self.checkDevise(devise)
        except TypeError:
            print("Values should be a number AND/OR same divise")
        except:
            print("Something else went wrong")
        else:
            self.valeur = newMonnaie
            return newMonnaie
        
        
    def retrancherMonnaie(self,monnaieRetrancher, devise):
        try:
            newMonnaie = self.retrancheDeuxNbre(self.valeur,monnaieRetrancher)
            self.checkDevise(devise)
        except TypeError:
            print("Values should be a number AND/OR same divise")
        except:
            print("Something else went wrong")
        else:
            self.valeur = newMonnaie
            return newMonnaie
    
    def ajouteDeuxNbr(self,nbr1, nbr2):
        return nbr1 + nbr2
            
    def retrancheDeuxNbre(self,nbr1, nbr2):
        return nbr1 - nbr2
    
    def checkDevise(self, newDevise):
        if(not self.devise):
            self.devise = newDevise
        elif(self.devise != newDevise):
           raise TypeError

    def test_ajouterMonnaie(self):
        self.clearMonnaie();
        assert self.ajouterMonnaie(5,'L.L') == 5, "Should be 5"
        assert self.ajouterMonnaie(7,'L.L') == 12, "Should be 12"
        self.clearMonnaie();
        print("Ajouter Monnaie passed")
        
    def test_retrancherMonnaie(self):
        self.clearMonnaie();
        assert self.ajouterMonnaie(5,'L.L') == 5, "Should be 5"
        assert self.retrancherMonnaie(7,'L.L') == -2, "Should be -2"
        self.clearMonnaie();
        print("Retrancher Monnaie passed")