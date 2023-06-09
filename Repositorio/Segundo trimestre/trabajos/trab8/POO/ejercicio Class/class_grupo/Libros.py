from Libros import *

class Libros:
    def __init__(self, tiulo, autor, numEstandar, publicacion):
    # super(Cuenta).__init__(librosPrestados,librosReservados, librosReservados, librosPrestados):
        self.tiulo = tiulo
        self.autor = autor
        self.numEstandar = numEstandar
        self.publicacion = publicacion
    
    def menulibros(self):
        while True:
            print(" ")
            print("1. La maldicion de hill house", 2017)
            print("2. It", "Estephen king", 2017)
            print("3. 1El resplandor", "Estephen king", 1977 )
            print("4. Psicología oscura, Steven turner", 2019)
            print("5. Las 48 leyes del poder, Robert Greene",1998)
            print("6. salir")
            print(" ")

            self.eleccion = input("digite su eleccion: ")
            print(" ")


            if self.eleccion == "1":
                print ("Titulo: El libro seleccionado fue La maldicion de hill house")
                print ("Autor: Shirley Jackson")
                print ("Año de publicacion: 1959")
                print ("informacion: La novela de Jackson utiliza el terror sobrenatural para provocar emoción en el lector, presentando relaciones complejas entre los eventos misteriosos en la casa y la psique de los personajes")


            elif self.eleccion == "2":
                print ("Titulo: El libro seleccionado fue It ")
                print ("Autor: Estephen king")
                print ("Año de publicacion: 2017")
                print("informacion:It es una novela de terror que Cuenta la historia, en un juego de correspondencias con el pasado y el presente, de un grupo de siete amigos")
            
            elif self.eleccion == "3":
                print("Titulo: El libro seleccionado fue El resplandor")
                print("Autor: Estephen king")
                print("Año de publicacion: 1977")
                print("informacion:El título se inspiró en la canción de John Lennon Instant Karma!, que contiene la línea «We all shine on...» (Todos brillamos en...")


            elif self.eleccion == "4":
                print("Titulo: El libro seleccionado fue Psicología oscura ")
                print("Autor: Steven turner")
                print("Año de publicacion: 2019 ")
                print("informacion:La psicología oscura hace referencia a las estrategias utilizadas para la manipulación y el control de los demás con el fin de alcanzar unos objetivos propios")
                        
            elif self.eleccion == "5":
                print("El libro seleccionado fue Las 48 leyes del poder")
                print("Robert Greene")
                print("Año de publicacion 1998")
                print("informacion:El libro es una guía diseñada para poder mostrarle al lector cuáles son las cualidades personales que se deben de tener para alcanzar el poder en términos sociológicos, un método práctico para todo aquel que quiera conseguir el poder, observe el poder, o tenga que defenderse del poder")
            
            elif self.eleccion=="6":
                print("chauuuuuu")
            else:
                print("Opción no válida. Vuelva a intentarlo" )
    # def lsls(self):
    #     self.titulo={titulo:autor}
    #     self.autor=
    #     isbn
    #     publicación
    #     estado

    #     def setISBN( self, isbn, titulo):
    #         values=list(titulo.keys())
    #         print(values)

    