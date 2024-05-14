def recursive_factorial(n):
        if n <= 1: # Abbruchbedingung
                return 1
        else:
                return n * recursive_factorial(n-1)
      
"""
Dokumentation von recursive_factorial(3):
recursive_factorial(3)
Die Abbruchbedingung ist nicht erfüllt.
Das Ergebnis von recursive_factorial(3) ist 3 * recursive_factorial(2).
Es muss zunächst recursive_factorial(2) ausgewertet werden.
        recursive_factorial(2)
        Die Abbruchbedingung ist nicht erfüllt.
        Das Ergebnis von recursive_factorial(2) ist 2 * recursive_factorial(1).
        Es muss zunächst recursive_factorial(1) ausgewertet werden.
                recursive_factorial(1)
                Die Abbruchbedingung ist erfüllt.
                Das Ergebnis von recursive_factorial(1) ist 1.
        Das Ergebnis von recursive_factorial(2) ist also 2 * 1 = 2
Das Ergebnis von recursive_factorial(3) ist also 3 * 2 = 6
"""

def recursive_sum_up(n):
        if n == 0: # Abbruchbedingung
                return n
        else:
                return n + recursive_sum_up(n-1)

"""
Dokumentation von recursive_sum_up(4):
recursive_sum_up(4)
Die Abbruchbedingung ist nicht erfüllt.
Das Ergebnis von recursive_sum_up(4) ist 4 + recursive_sum_up(3).
Es muss zunächst recursive_sum_up(3) ausgewertet werden.
        recursive_sum_up(3)
        Die Abbruchbedingung ist nicht erfüllt.
        Das Ergebnis von recursive_sum_up(3) ist 3 + recursive_sum_up(2).
        Es muss zunächst recursive_sum_up(2) ausgewertet werden.
                recursive_sum_up(2)
                Die Abbruchbedingung ist nicht erfüllt.
                Das Ergebnis von recursive_sum_up(2) ist 2 + recursive_sum_up(1).
                Es muss zunächst recursive_sum_up(1) ausgewertet werden.
                        recursive_sum_up(1)
                        Die Abbruchbedingung ist nicht erfüllt.
                        Das Ergebnis von recursive_sum_up(1) ist 1 + recursive_sum_up(0).
                        Es muss zunächst recursive_sum_up(0) ausgewertet werden.
                                recursive_sum_up(0)
                                Die Abbruchbedingung ist erfüllt.
                                Das Ergebnis von recursive_sum_up(0) ist 0
                        Das Ergebnis von recursive_sum_up(1) ist also 1 + 0 = 1.
                Das Ergebnis von recursive_sum_up(2) ist 2 + 1 = 3.
        Das Ergebnis von recursive_sum_up(3) ist 3 + 3 = 6.
Das Ergebnis von recursive_sum_up(4) ist 4 + 6 = 10.                                     
"""

def fib(n):
# Eine Funktion zur Berechnung der n-ten Fibonaccizahl
        if n == 0:
                return 0
        elif n == 1:
                return 1
        else:
                return (fib(n-1) + fib(n-2))
        
def is_even(n):
# Diese Funktion überprüft durch rekursive Aufrufe von is_odd und indirekt sich selbst, ob eine n gerade ist
        if n == 0:
                return True
        else:
                return is_odd(n-1)
        
def is_odd(n):
# Diese Funktion überprüft durch rekursive Aufrufe von is_even und indirekt sich selbst, ob eine n ungerade ist
        if n == 0:
                return False
        else:
                return is_even(n-1)