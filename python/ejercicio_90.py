import time
def main():

    h= int(input("ingrese las horas: "))
    m= int(input("ingrese los minutos: "))
    s= int(input("ingrese los segundos: "))

    for i in range(h):
        for j in range(60):
            for k in range(60):
                print("{}:{}:{}".format(i,j,k))
                time.sleep(1)
                
    
    for i in range(m):
        for j in range(60):
            print("{}:{}:{}".format(h,i,j))
            time.sleep(1)
            

    for i in range(s):
        print("{}:{}:{}".format(h,m,i))
        time.sleep(1)
        

if __name__ == "__main__":
    main()
    
