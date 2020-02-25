import io

def leer():
    archivo= open("archivo.txt","r")
    texto = archivo.read()
    archivo.close()
    print(texto)
    
    

def main():
    leer()
    

if __name__ == "__main__":
    main()
