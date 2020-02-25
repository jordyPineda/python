import io

def escribir():
    archivo= open("archivo.txt","w")
    for i in range(33,225):
        a= chr(i)
        archivo.write(a)
        
    archivo.close()
    

def main():
    escribir()
    

if __name__ == "__main__":
    main()
