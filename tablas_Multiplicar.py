class tablas:
    def imprimir_tabla(self):
     
        for i in range (1,10):
            LIMITE = 10
            contador = 1
            print(" ")
            while contador <= LIMITE:
                resultado = contador * i
                print("{} x {} = {}".format(i, contador, resultado))
                contador = contador + 1
            
    
tabla=tablas()
tabla.imprimir_tabla()
