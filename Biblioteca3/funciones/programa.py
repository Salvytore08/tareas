def programa():
    """
        Esta función es la que contiene toda la lógica del programa
    
    """
    import time
    import Menú
    from clase import Persona
   
    while True:
        Menú.menu()
        a = int(input('Por favor ingrese la opción que desea: '))
        time.sleep(1.2)

        match a:
            case 1:
                id = input('Por favor ingrese su ID de usuario: ')
                nom = input('Por favor ingrese el nombre del usuario: ')
                nom = Persona(id, nom)
                print('Usuario añadido con éxito')
            
            case 2:
                nom = input('Por favor ingrese el nombre del libro: ')
                fecha = input('Por favor ingrese la fecha de hoy: ')
                nom.añadir(nom,fecha)
                print('Libro prestado con éxito')
            
            case 3:
                x = input('Por favor ingrese el usuario que desea eliminar: ')
                nom.eliminar_usu(x)
            
            case 4:
                x = input('Por favor ingrese el libro que desea devolver: ')
                nom.eliminar(x)
                print('Libro devuelto con éxito')
            
            case 5:
                nom.ver()
            
            case 6:
                a = input('Puede salir (Presione ENTER para salir)')
                break
            
            case _:
                print('Opción no válida')
                time.sleep(1.2)
