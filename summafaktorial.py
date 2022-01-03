# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:22:49 2022

@author: Pilotech
"""

class Summa():
    def __init__(self,n):
        self.n=int(n)
    
    def give(self,savol):
        savol=self.n
        return savol

    def get_n(self):
        return self.n  

    def summa(self):
        yigindi=0
        for self.n in range(1,self.n+1):
            yigindi+=self.faktor(self.n)
        return yigindi
    def faktor(self,n):
        son=1
        a=list(range(2,self.n+1))
        for i in a:
            son*=i
        return son  
savol=" yig'indisini ko'rsatadi: "
sonlar=int(input("Son kiriting va men ungacha bo'lgan sonlarning faktorialllari"+savol))
javob=Summa(sonlar)
print(javob.summa())
input("")   
