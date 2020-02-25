

def main():
    
    a= int(input("ingrese un numero: "))
    b= int(input("hasta que numero decea la tabla: "))
    
    for i in range(b+1):
        print(" {} * {} = {}".format(a,i,a*i))
    

if __name__ == "__main__":
    main()
