class parImpar:
    def num(self):
        nu = input("Introduce un número: ")
        
        nu = int(nu)
        if nu == 0:
            print ("Este número es par.")
        elif nu%2 == 0:
            print ("Este numero es par")
        else:
            print ("Este numero es impar")

   
par=parImpar()
par.num()
