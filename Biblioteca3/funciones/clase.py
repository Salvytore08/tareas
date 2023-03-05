import Menú	
import time

class Persona():
    
    def __init__(self,id,nombre):
        self.id = id
        self.nom = nombre
        self.info = {
            'ID' : self.id,
            'Nombre' : self.nom,
            'Libros': []
        }
    
    def añadir(self,libro,fecha):
        nuevo_libro = {
            'Nombre' : libro,
            'Fecha' : fecha,
            'Estado' : 'Prestado'
        }
        self.info['Libros'].append(nuevo_libro)
        
    def ver(self):
        print('\n')
        for i,j in self.info.items():
            if i == 'Libros':
                print('\n')
                for i in range(len(self.info['Libros'])):
                    for i,j in self.info['Libros'][i].items():
                        print(f'\t{i} : {j}')
                    print('\n')
                break
            print(f'{i} : {j}')
            
    def eliminar(self,libro):
        for i in range(len(self.info['Libros'])):
            if self.info['Libros'][i]['Nombre'] == libro:
                self.info['Libros'][i]['Estado'] = 'Devuelto'

    def eliminar_usu(self):
        del self



