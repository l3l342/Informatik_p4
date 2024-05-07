"""
Insertion Sort:
Insertionsort entnimmt der unsortierten Eingabefolge ein beliebiges Element
und fügt es an richtiger Stelle in die (anfangs leere) Ausgabefolge ein.
Geht man hierbei in der Reihenfolge der ursprünglichen Folge vor, so ist
das Verfahren stabil. Wird auf einem Array gearbeitet, so müssen die
Elemente hinter dem neu eingefügten Element verschoben werden.
"""

def insertion_sort(list):
        sorted_list = [list[0]]
        list.pop(0)
        while len(list) > 0:
                index = 0
                elem = list.pop()
                while index < len(sorted_list) and elem > sorted_list[index]: # >:min_sort      <:max_sort
                        index += 1
                sorted_list = sorted_list[0:index] + [elem] + sorted_list[index:len(sorted_list)]
        return sorted_list

def swap(list,i,j):
        #Vertauscht das i-te mit dem j-ten Element einer Liste
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        return list

def isort(list):
        #Insertion Sort mit Swap (Liste wird direkt sortiert)
        for position in range(len(list)):
                index = position
                while index > 0 and list[index] < list[index-1]: # <:min_sort      >:max_sort
                        swap(list,index,index-1)
                        #print(list) # Sortierschritte
                        index -= 1   
        return list

list=[6,3,8,54,3,8,34,7]

print(isort(list))