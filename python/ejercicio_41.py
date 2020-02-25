
def main():
    v=0
    c=0
    n=0
    vocales=("a","e","i","o","u")
    consonantes=("b","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","y","z")
    entrada= raw_input("ingrese una cadena de caracteres: ")
    for i in vocales:
        for j in range(len(entrada)):
            if entrada[j]== i:
                v=v+1
    for i in consonantes:
        for j in range(len(entrada)):
            if entrada[j]== i:
                c=c+1
    n=len(entrada)-v-c
    print("cantidad de vocales: {}".format(v))
    print("cantidad de consonantes: {}".format(c))    
    print("cantidad de caracteres que no pertenecen a ninguno de los anteriores: {}".format(n))

if __name__ == "__main__":
    main()
