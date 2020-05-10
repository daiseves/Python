frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE 
archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada 
con interfaz gráfica, o UN juego simple.'''

dic={}
list=[]

frase = frase.replace(',','')
frase = frase.replace('.', '').lower()
frase = frase.split()


for i in frase:
    if len(i) not in dic.keys():
        list = [i]
        dic[len(i)] = list
    else:
        if i not in dic[len(i)]:
            dic[len(i)].append(i)
print(dic)
    
