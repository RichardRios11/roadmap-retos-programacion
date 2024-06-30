'''
Estructura de Datos
'''

'''
             ********  Lista  *************
Lista, es una estructura ordenada donde se almacenas o muestran datos
se puueden aliminar, reemplazar, agregar y ordenacion (como se inserta)
'''
my_list = ["Brais", "Richard", "Yulevis", "Andres"]
print(type(my_list))
print(my_list)
my_list.append("Ricardo") # insertar
print(my_list)
my_list.remove("Brais")  # eliminacion
print(my_list)
print(my_list[1])
my_list[1] = "Yuli"   # actualizacion 
print(my_list)
my_list.sort()
print(my_list)


'''
             ********  Tuplas  *************
Tupla, es una estructura que se pueden guardar mas de un dato
pero como se cree la tupla no se puede modificar
'''
my_tuple: tuple = ("Richard", "Rios", "Richarddev", "50") # definicion, tambien se puede asi
print(type(my_tuple))
print(my_tuple[1])
print(my_tuple[2])
my_tuple = tuple(sorted(my_tuple))
'''
sorted es del sistema y de vuelve una lista en este
se convierte a tupla de nuevo, sorted no soporta numeros y string
por eso para hacer la prueba se convierte a string el numero 
'''  
print(my_tuple)

'''
             ********  Sets  *************
Set, es una estructura que se pueden guardar, pero por definicion
es una estructura desordenada, no nos podemos fiar de la posicion donde se 
encuentra un elemento, no acepta repetidos
'''
my_set = {"Richard", "Rios", "Richarddev", "50"}
print(type(my_set))
print(my_set)
my_set.add("richard@gmail.com")
my_set.add("richard@gmail.com")  # no acepta repetidos
my_set.add("richard@hotmail.com") 
my_set.add("A")
#print(my_set[2]) no se puede acceder asi porque no tiene logica porque varia
print(my_set)
my_set.remove("richard@hotmail.com")
print(my_set)
my_set = set(sorted(my_set)) # el set no una estructura ordenada, no se puede ordenar
print(my_set)
print(type(my_set))

'''
             ********  Dict  *************
Diccionario, es una estructura que se pueden guardar, pero por definicion
es una estructura desordenada, no nos podemos fiar de la posicion donde se 
encuentra un elemento, no acepta repetidos, los diccionarios en puthon son
ordenados
'''

my_dict = {
    "name": "Richard", 
    "surname" :"Rios", 
    "url" :"Richarddev", 
    "age" :"50"
    }
print(type(my_dict))
print(my_dict)
print(my_dict["name"])  #acceso
my_dict["city"] = "Maracaibo" # inserccion y actualizacion
print(my_dict)
my_dict["age"] = "51" #actualizacion
print(my_dict)
del my_dict["city"]
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # ordenacion 
print(my_dict)
#var =my_dict[0]
#print(var) error

'''
             ********  Extra  *************

'''

def my_agenda():
    agenda = {}

    def search_name(add="none"):
        name = input("Ingrese el nombre del contacto: ")
        if name in agenda:
            if add=="none":
                return name
            else:
                input(f"El contacto '{name.upper()}' ya existe, presione Enter")
                return None
        elif add=="add":
            return name
        else:
            input(f"El contacto '{name.upper()}' no existe, presione Enter")
            

    def verify_phone(name:str, phone:str, case:str):
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
            input(f"El contacto '{name.upper()}' se {"ingreso" if case == "2" else "actualizo"} correctamente, presione Enter ")
        else:
            input(f"**Error***, Verifique el numero de telefono '{phone}', presione Enter")

    def search_contact():
        name= search_name()
        if name:
            input(f"El numero de telefono del contacto '{name.upper()}' es '{agenda[name]}', presiones ENTER")

    def add_contact():
        name = search_name("add")
        if name != None:
            phone = input("Ingrese el telefono del contacto: ")
            verify_phone(name, phone, "2")

    def uppdate_contact():
        name = search_name()
        if name:
            phone = input(f"Actualice el telefono del contacto '{name.upper()}'actualizado: ")
            verify_phone(name, phone, "3")

    def del_contact():
        name = search_name()
        if name:
            del agenda[name]
            input(f"El numero de telefono del contacto '{name.upper()}'se ha eliminado, presione ENTER")

    while True:
        print("")
        print("****** AGENDA DE TELEFONO ******")
        print("")                                                
        print("1.- Buscar contacto")
        print("2.- Insertar contacto")
        print("3.- Actualzar contacto")
        print("4.- Eliminar contacto")                                                       
        print("5.- Finalizar")                                                                               
        
        option = input("\nIngrese su opcion: ")
        match option:
            case "1":
                search_contact()
            case "2":
                add_contact()
            case "3":
                uppdate_contact()
            case "4":
                del_contact()
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                input("Opcion no valida, elige una opcion del 1 al 5, presione una tecla")
                
my_agenda()
