import math
def distancia(x1,y1,x2,y2):
    x=pow(x2-x1,2)
    y=pow(y2-y1,2)
    d=x+y
    d=math.sqrt(d)
    return d
    

def main():
    x1= int(input("Ingrese la cordenada x del primer punto: "))
    y1= int(input("Ingrese la cordenada y del primer punto: "))
    x2= int(input("Ingrese la cordenada x del segundo punto: "))
    y2= int(input("Ingrese la cordenada y del segundo punto: "))
    s=distancia(x1,y1,x2,y2)

    print("la distancia entre los dos puntos es: {}".format(s))

if __name__ == "__main__":
    main()
