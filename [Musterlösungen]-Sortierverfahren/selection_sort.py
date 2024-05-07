"""
Selection Sort:
Sei S der sortierte Teil des Arrays (vorne im Array) und U der unsortierte
Teil (dahinter). Am Anfang ist S noch leer, U entspricht dem ganzen
(restlichen) Array. Das Sortieren durch Auswählen läuft nun folgendermaßen
ab:
Suche das kleinste Element in U und vertausche es mit dem ersten Element
von U (= das erste Element nach S).
Danach ist das Array bis zu dieser Position sortiert. Das kleinste Element
wird in S verschoben (indem S einfach als ein Element länger betrachtet
wird, und U nun ein Element später beginnt). S ist um ein Element
gewachsen, U um ein Element kürzer geworden. Anschließend wird das
Verfahren so lange wiederholt, bis das gesamte Array abgearbeitet worden
ist; S umfasst am Ende das gesamte Array, aufsteigend sortiert, U ist leer.
"""

def selection_sort(list):
        #list wird schrittweise geleert, sorted_list ist die sortierte Liste
        sorted_list = []
        while len(list) > 0:
               index = smallest_value_index(list)
               sorted_list.append(list[index])
               list.pop(index)
        return sorted_list
               
def smallest_value_index(list):
        index = 0
        for i in range (1,len(list)):
                if list[i] < list[index]:
                        index = i
        return index

def swap(list,i,j):
        #Vertauscht das i-te mit dem j-ten Element einer Liste
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        return list

def ssort(list):
        #Selection Sort mit Swap (Liste wird direkt sortiert)
        for i in range(len(list)):
                swap(list,i,i + smallest_value_index(list[i:len(list)]))
        return list

list=[6,3,8,54,3,8,34,7]
print(ssort(list))
print(selection_sort(list))