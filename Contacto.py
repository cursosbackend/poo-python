import os


class Contacto:
    def __init__(self, nombre:str, email:str, telefono:str) -> None:
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono


    @property
    def nombre(self):
        return self.__nombre
    @property
    def email(self):
        return self.__email
    @property
    def telefono(self):
        return self.__telefono
    

    def __repr__(self):
        return repr([self.nombre,self.email,self.telefono])
    


class ContactoTrabajo(Contacto):
    
    #constructor del ContactoTrabajo()
    def __init__(self, nombre, email, telefono, empresa, oficio):
        # constructor  de Contacto()
        super().__init__(nombre, email, telefono)
        self.__empresa = empresa
        self.__oficio = oficio

    
    @property
    def empresa(self):
        return self.__empresa
    
    @property
    def oficio(self):
        return self.__oficio

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
        return ContactoTrabajo(nombre,telefono,email,empresa,oficio)
    

class App:
    def __init__(self):
        self.manejador = Manejador()



    def run(self):
        while True:
            Consola_menu.limpiar_consola()
            Consola_menu.mostrar_menu()\
            
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
            input("enter para continuar")

                


















app = App()
app.run()






    



        

    



 









            

        
    




    



    

    

    





