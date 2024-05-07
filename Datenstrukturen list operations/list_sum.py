liste = [1,2,3,4,5]
summe = 0
for elem in liste:
        summe = summe + elem
print(summe)
summe = 0

#ODER:

for i in range(len(liste)):
        summe = summe + liste[i]        
print(summe)