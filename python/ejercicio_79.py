def suma(a):
    if a==0:
        return 0
    else:
        return a + suma(a-1)


def main():

    a= int(input("ingrese un numero (-1 para salir): "))
    while a >= 0:
        s= suma(a)
        print("la suma de los primeros {} numeros naturales es: {}".format(a,s))
        a= int(input("ingrese un numero (-1 para salir): "))


if __name__ == "__main__":
    main()
