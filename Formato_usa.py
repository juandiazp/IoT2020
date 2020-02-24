class califi:
    def num(self):
        var=input("Dame un número entre 0 y 10: ")
        
        var = int(var)
        if(var == 0):
            print("cero")
        elif(var == 1):
            print("uno")
        elif(var == 2):
            print("Dos")
        elif(var == 3):
            print("Tres")
        elif(var == 4):
            print("Cuatro")
        elif(var == 5):
            print("Cinco")
        elif(var == 6):
            print("Seis")
        elif(var == 7):
            print("Siete")
        elif(var == 8):
            print("Ocho")
        elif(var == 9):
            print("Nueve")
        elif(var == 10):
            print("Diez")
        else:
            print("numero erroneo")


    

calificacion=califi()
calificacion.num()
