import math

def longitud(r):
    s= math.pi*2*r
    return s

def area(r):
    s= math.pi* pow(r,2)
    return s

def main():
    r = float(input("ingrese el radio:  "))
    print("la longitud de la circunferencia es: {}".format(longitud(r)))
    print("el area de la circunferencia es: {}".format(area(r)))

if __name__ == "__main__":
    main()
    
