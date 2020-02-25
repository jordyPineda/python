
def main():
    ingreso= raw_input("Ingrese una frase: ")
    no_espacio=""
    for i in range(len(ingreso)):
        if ingreso[i]!= " ":
            no_espacio= no_espacio + ingreso[i]
    print("la frase ingresada es: "+ingreso)
    print("la frase ingresada sin espacios es: "+no_espacio)


if __name__ == "__main__":
    main()
