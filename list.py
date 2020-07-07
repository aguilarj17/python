from io import open
#First  all the file .txt and givw if its for read write
order = open('list.txt','r', encoding="utf8")
#pass to a pointer and can read the lines
lineas = order.readlines()
#close the file
order.close()

personas = []
for linea in lineas:
    #eliminate line breaks and spaces
    campos = linea.replace("\n"," ").split(";")
    persona = {"id":campos[0], "nombre":campos[1], 
               "apellido":campos[2], "nacimiento":campos[3]}
    personas.append(persona)
#for print
for p in personas:
    print("(id={}) {} {} => {} ".format( p['id'], p['nombre'], 
                                         p['apellido'], p['nacimiento']) )
