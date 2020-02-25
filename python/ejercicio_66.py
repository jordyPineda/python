
def factorial(a):
    s=1;
    if a==0:
        return 1
    else:
        for i in range(1,a+1):
            s=s*i
        return s

    

def main():
    a=0
    a=int(input("ingrese un numero (-1 para salir): "))
    while( a!= -1):
        b= factorial(a)
        print("el factorial es: {}".format(b))
        a=int(input("ingrese un numero (-1 para salir): "))

    

if __name__ == "__main__":
    main()
