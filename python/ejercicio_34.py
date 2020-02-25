

def main():
    a=1
    par=0
    impar=0
    
    while a != 0:
        a= int(input("ingrese un numero: "))
        if a<0:
            a = a * -1
        if (a%2) == 0:
            par = par + a
        else:
            impar = impar +a
        print("suma de los numeros pares {}".format(par))
        print("suma de los numeros impares {}".format(impar))      
    
if __name__ == "__main__":
    main()
