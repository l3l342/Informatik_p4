def linear_search(liste,n):
# Diese Funktion gibt den Index eines enthaltenen Elements wieder oder "Nicht enthalten"
        for index in range(len(liste)): #PP01 Liste wird elementweise durchsucht
                if liste[index] == n: #PP02 Bedingung: Listenelement == gesuchtes Element
                        return index # Wenn Bedingung erfüllt -->Rückgabe des Index
        
        return "Nicht enthalten" # Ausgabe, falls Element nicht enthalten ist
                
print(linear_search([9,6,8,7,5,3,4,1],11))

"""
Programmtabelle für liste = [3,4,7,5] und n = 7
PP      index       liste[index] == n           return
#1
"""