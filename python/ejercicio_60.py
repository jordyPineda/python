
def main():
    abecedario= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                 "v", "w", "x", "y", "z"]
    c = []
    for i in range(26):
        c.append(0)
    ingreso = raw_input("ingrese una frase: ")

    for i in range(26):
        for j in range(len(ingreso)):
            if ingreso[j]==abecedario[i]:
                c[i]= c[i]+1
    
    for i in range(26):
        print("la letra {} aparecio {} veces ".format(abecedario[i],c[i]))
    

if __name__ == "__main__":
    main()
