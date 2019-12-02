import re

coincidencias_num = re.findall(
    '\d+',
    str(
        "'192.165.34.23'= 1234"
    )
)


print(coincidencias_num)


class File:
    def __init__(self, nom_archivo, nom_modo):
        self.nom_archivo = nom_archivo
        self.nom_modo = nom_modo

    def __enter__(self):
        self.open_file = open(self.nom_archivo, self.nom_modo)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()


def escribir_archivo(nom_archivo, dato):
    datos = []
    with File(nom_archivo, 'a') as archivo:
        archivo.write(str(dato) + ',')
        datos.append(archivo)


escribir_archivo('PRUEBA_ESCRITURA2.txt', 'dato2')
