def main():
    print("Fibonacci:")
    fibonacci(0, 1, 100)
    print(f"\nFattoriale di 5:\n{fattoriale(5)}")
    print(f"\n MCD 49 - 28:\n{mcd(49, 28)}")
    
def fibonacci(i, j, end):
    somma = i + j
    if somma > end:
        return
    print(somma)
    fibonacci(j, somma, end)
    
def fattoriale(a):
    if a == 0:
        return 1
    return a * fattoriale(a - 1)

def mcd(x, y):
    print(f" - resto di {x}/{y} = {x % y}")
    if x % y == 0:
        return y
    return mcd(y, x % y)

main()