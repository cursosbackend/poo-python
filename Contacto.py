import os



class Contacto:
    def __init__(self, nombre:str, email:str, telefono:str) -> None:
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre
    @property
    def email(self):
        return self._email
    @property
    def telefono(self):
        return self._telefono
    

    def __repr__(self):
        return repr([self.nombre,self.email,self.telefono])
    


class ContactoTrabajo(Contacto):
    
    #constructor del ContactoTrabajo()
    def __init__(self, nombre, email, telefono, empresa, oficio):
        # constructor  de Contacto()
        super().__init__(nombre, email, telefono)
        self._empresa = empresa
        self._oficio = oficio

    
    @property
    def empresa(self):
        return self._empresa
    
    @property
    def oficio(self):
        return self._oficio

    def __repr__(self):
        return  repr([f"{self.nombre} , {self.email},{self.telefono} ,{self.empresa}, {self.oficio}"])
        


class Manejador:

    def __init__(self):
        self.contactos:list[Contacto] = []

    
    def agregar_contacto(self, contacto:Contacto):
        self.contactos.append(contacto)

    def listar_contactos(self) -> list[Contacto]:
        return self.contactos
                                #Juanito
    def buscar_contacto(self, nombre):
        nombre_minuscula  = nombre.lower()
        for i in self.contactos:
            if i.nombre.lower() == nombre_minuscula:
                return i
        return None
    

    def actualizar_contacto(self, nombre , telefono , email):
        c = self.buscar_contacto(nombre)
        
        c._telefono = telefono
        c._email = email
        return c
    
    def borrar_contacto(self,nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto is not None:
            self.contactos.remove(contacto)
            


class Consola_menu:
    #1. limpiar la consola
    #2. mostrar menu
    @staticmethod
    def limpiar_consola():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def mostrar_menu():
        print("""
=== menu contactos ===
              
1. Agregar contacto
2. Agregar contacto trabajo
3. Listar contactos
4. Buscar usuario
5. Actualizar usuario
6. Eliminar usuario
8. Salir
""")


class Pedir_datos:

    @staticmethod
    def contacto_normal():
        nombre = input("nombre :")
        email = input("email :")
        telefono = input("telefono :")
        return Contacto(nombre,telefono,email)

    @staticmethod
    def contacto_empresa():
        nombre = input("nombre :")
        email = input("email :")
        telefono = input("telefono :")
        empresa = input("empresa :")
        oficio = input("oficio :")
        return  (nombre,telefono,email,empresa,oficio)
    

class App:
    def __init__(self):
        self.manejador = Manejador()



    def run(self):
        while True:
            Consola_menu.limpiar_consola()
            Consola_menu.mostrar_menu()
            
            opcion = input("Elige una opcion : ")

            if opcion == "1":
                 c = Pedir_datos.contacto_normal()
                 self.manejador.agregar_contacto(c)
                 print("contacto agregado!!")
                 

            elif opcion == "2":
                ct = Pedir_datos.contacto_empresa()
                self.manejador.agregar_contacto(ct)
                print("contacto agregado!!")
                

            elif opcion =="3":
                contactos = self.manejador.listar_contactos()
                if contactos:
                    for i in contactos:
                        print(i)
                else:
                    print("sin contactos")
                    


            elif opcion == "4":
                nombre = input("nombre contacto : ")
                c = self.manejador.buscar_contacto(nombre)
                if c:
                     print(c)
                else:
                    print("contacto no encontrado!")


            elif opcion == "5":
                nombre = input("nombre a actualizar")
                telefono = input("nuevo telefono")
                email = input("nuevo correo")
                c = self.manejador.actualizar_contacto(nombre, telefono, email)            
                print("contacto actualizado")

            elif opcion == "6":
                nombre = input("contacto a borrar")
                c = self.manejador.borrar_contacto(nombre)
                print("contacto borrado")

            elif opcion == "7":
                Consola_menu.limpiar_consola()
                print("adiossss")
                exit()
                

            else:
                print("opcion no valida")





                




















                
            input("enter para continuar")
                    






                


















app = App()
app.run()






    



        

    



 









            

        
    




    



    

    

    





