#ejercicio 6_2
#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como 
#atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, 
#imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado

class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

#funcion para imprimir

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

#funcion si aprobo o no

    def resultado(self):
        if self.nota < 7:
            print("El alumno a desaprobado")
        else:
            print("El alumno aprobo")


#bloque principal

alumno1 = Alumno()
alumno2 = Alumno()
alumno3 = Alumno()

#inicializamos

alumno1.inicializar("Alejandro", 5)
alumno2.inicializar("Ger", 8)
alumno3.inicializar(input("Ingrese nombre:" ),int(input("Ingrese nota:" )))


#imprimir

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
alumno3.imprimir()
alumno3.resultado()