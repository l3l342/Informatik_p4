def binary_search(liste,n):
        min = 0
        max = len(liste) - 1
        while min <= max:
                mid = (max + min) // 2
                if liste[mid] > n:
                        max = mid - 1
                elif liste[mid] < n:
                        min = mid + 1
                else:
                        return mid
        return "Nicht enthalten!"

def recursive_binary_search(liste,n): # Überprüfung ob Element enthalten, keine Indexausgabe!
        if len(liste) == 0:
                return False
        else:
                mid = (len(liste)) // 2
                
                if liste[mid] == n:
                        return True
                else:
                        if liste[mid] < n:
                                return recursive_binary_search(liste[mid+1:],n)
                        else:
                                return recursive_binary_search(liste[:mid],n)

print(recursive_binary_search([1,2,3,4,5,6,7,9],10))