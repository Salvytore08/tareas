class Persona():
    
    def __init__(self,id,nombre):
        self.id = id
        self.nom = nombre
        self.info = {
            'ID' : self.id,
            'Nombre' : self.nom,
            'Libros': []
        }
        
    def __str__(self):
        num_libros = len(self.info['Libros'])
        return f'{self.id} : {self.nom} tiene {num_libros} libros prestados'
    
    def agregar(self,libro,fecha):
        nuevo_libro = {
            'Nombre' : libro,
            'Fecha' : fecha,
            'Estado' : 'Prestado'
        }
        self.info['Libros'].append(nuevo_libro)
        
    def ver(self):
        for i,j in self.info.items():
            print(f'{i} : {j}')
            
    def eliminar(self,libro):
        for i in self.info['Libro']:
            if i['Nombre'] == libro:
                print('Si está')
            
yo = Persona('15018', 'Principito')
yo.agregar('15017', 'Hábitos Atómicos')
yo.ver
