
def multiplicar(a,b):
    return a*b

def divicion(a,b):
    return a/b

def main():
    a = int(input("ingrese un numero:  "))
    b = int(input("ingrese otro numero:  "))
    print("la suma es {}".format(a+b))
    print("la resta es {}".format(a-b))
    print("la multiplicacion es: "+ str(multiplicar(a,b)))
    print("la divicion entera de {}/{} da {}".format(a,b,divicion(a,b)))

if __name__ == "__main__":
    main()
    
