#con append podemos agregar más informacion al archivo

dataFile = open('.\sample_two.txt', "a")

for i in range(1,4):
    dataFile.write(f"a la {i} \n")

dataFile.close()