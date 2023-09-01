# leer un archivo con open()
data = open('.\sample.txt', 'r')

# leemos el contenido con el metodo read()
print(data.read())

#inportante cerrar el archivo
data.close()