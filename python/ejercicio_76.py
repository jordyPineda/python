
def factorial(a):
    if a==0:
        return 1
    else:
        return a * factorial(a-1)

def main():
    a= int(input("ingrese un numero (-1 para salir): "))
    while a >= 0:
        s= factorial(a)
        print("el factorial de {} es: {}".format(a,s))
        a= int(input("ingrese un numero (-1 para salir): "))
    

if __name__ == "__main__":
    main()
