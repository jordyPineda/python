
def descuento(a):
    if a<=20000:
       print("no tiene descuento, total a pagar {}".format(a)) 
    else:
        
        s=a*0.15
        s=a-s
        print("tiene un descuento del 15% en la fatura, total a pagar {}".format(s))

def main():
    a = int(input("ingrese el importe bruto de la factura :  "))
    descuento(a)

if __name__ == "__main__":
    main()
    
