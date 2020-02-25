import modulo_81

def main():
    x=1

    while x!=0:
        a= int(input("ingrese el primer numero: "))
        b= int(input("ingrese el segundo numero: "))
        s= modulo_81.suma(a,b)
        print("la suma de {} y {} es: {}".format(a,b,s))
        s= modulo_81.resta(a,b)
        print("la resta {}-{} es: {}".format(a,b,s))
        s= modulo_81.multiplicacion(a,b)
        print("la multiplicacion de {} y {} es: {}".format(a,b,s))
        s= modulo_81.divicion(a,b)
        print("la divicion {}/{} es: {}".format(a,b,s))
        s= modulo_81.potencia(a,b)
        print("la potencia {}^{} es: {}".format(a,b,s))
        x= int(input("ingrese 0 si decea salir: "))
    

if __name__ == "__main__":
    main()
