# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:50:53 2019

@author: mina2
"""

class Fraction:

    def fraction(self, nbr1, nbr2):
        try:
            return nbr1*nbr2**-1
        except:
            print('Division par zero')
            
    def simplifie(self, nbr1,nbr2):
        nbr1 = self.decompose(nbr1)
        nbr2 = self.decompose(nbr2)


    def decompose(self,n): 
        res=[]
        i=2 
        while n>1: 
            while n%i==0: 
               res += [i]
               n=n/i 
            i=i+1 
        return res
