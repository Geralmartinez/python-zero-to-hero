#para escrivir utilizamos el modo w con la funcion open

data = open('sample_two.txt', 'w')

for i in range(4):
   data.write(f"hola pescao {i} \n")

data.close()