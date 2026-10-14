def buscar(nodo, objetivo):
            if not nodo:
                return False
            if nodo.val == objetivo:
                return True
            return buscar(nodo.sig, objetivo)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    print(factorial(5))