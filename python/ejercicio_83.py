import modulo_83

def main():

    x="si"

    while x=="si":
        a = raw_input("Igrese un  numero en binario ")
        b = raw_input("Igrese otro  numero en binario ")
        s = modulo_83.suma(a,b)
        r= modulo_83.resta(a,b)
        d = modulo_83.dividir(a,b)
        m = modulo_83.multiplicar(a,b)

        print 'la suma es: ',
        print bin(s)
        print("corresponde en decimal a: {}".format(s))
        print 'la resta es: ',
        print bin(r)
        print("corresponde en decimal a: {}".format(r))
        print 'la divicion es: ',
        print bin(d)
        print("corresponde en decimal a: {}".format(d))
        print 'la multiplicacion es: ',
        print bin(m)
        print("corresponde en decimal a: {}".format(m))
        x=raw_input("decea ingresar otros numeros? (si/no): ")

    
if __name__ == "__main__":
    main()
