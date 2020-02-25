import time

def main():
    h= int(input("ingrese las horas: "))
    m= int(input("ingrese los minutos: "))
    s= int(input("ingrese los segundos: "))

    while s> 0:
        s=s-1
        print("{}:{}:{}".format(h,m,s))
        time.sleep(1)

    while m > 0:
        m=m-1
        c=60
        while c>= 0:
            print("{}:{}:{}".format(h,m,c))
            c=c-1
            time.sleep(1)

    
    while h > 0:
        h=h-1
        a=59
        while a >= 0:
            i=59
            while i>= 0:
                print("{}:{}:{}".format(h,a,i))
                i=i-1
                time.sleep(1)
            a=a-1

    

    

if __name__ == "__main__":
    main()
