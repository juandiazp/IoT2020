#Creando clase area: AreaTrapecio.PY

class Area:
    def _init_(self):
        self.h = 0
        self.a = 0
        self.b = 0
        self.r = 0
    def areatrapecio(self):
        self.r = ((self.a+self.b)*self.h)/2
        
    def areatriangulo(self):
        self.r = (self.b*self.h)/2
        
    def areacirculo(self):
        self.a = 3.1416*(self.r*self.r)

    
T=Area()
T.h=2
T.a=3
T.b=5
T.areatrapecio()
print("El área del trapecio es: " + str(T.r))

at=Area()
at.h=16
at.b=20
at.areatriangulo()
print("El área deñ triangulo es: " + str(at.r))

ac=Area()
ac.r=1
ac.areacirculo()
print("El área del circulo es: " + str(ac.a))
