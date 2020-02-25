
def main():
    a = int(input("ingrese el primer numero:  "))
    b = int(input("ingrese el segundo numero:  "))
    c = int(input("ingrese el tercer numero:  "))

    if a<b:
        if b<c:
            print("ingreso los numeros en orden creciente")
    else:
        if a>b:
            if b>c:
                print("ingreso los numeros en orden decreciente")
        else:
            print("no ingreso los numeros en ningun orden")
   

if __name__ == "__main__":
    main()
    

