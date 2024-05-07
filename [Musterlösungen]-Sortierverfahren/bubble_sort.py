"""
Bubble Sort:
Sortieren durch Aufsteigen
Da die Elemente paarweise verglichen und ggf. getauscht werden,
sollte Bubble Sort direkt mit swap() programmiert werden.
Programmierungen wie bei Insertion und Selection Sort mit neuem Array
machen hier wenig Sinn.
"""
def swap(list,i,j):
        #Vertauscht das i-te mit dem j-ten Element einer Liste
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        return list

def bsort(list):
        index = len(list)
        while index > 0:
                for i in range(len(list)-1):
                        if list[i] >= list[i+1]:
                                swap(list,i,i+1)
                        #print(list) # Sortierschritte
                index -= 1
        return list
                
                

list=[6,3,8,54,3,8,34,7]

print(bsort(list))