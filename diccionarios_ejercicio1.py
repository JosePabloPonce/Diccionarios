#Jose Pablo Ponce, 19092
#20-02-19
#diccionarios_ejercicio1
#programa que al ingresar 3 numeros en texto en rango del 1 al 10 los traduzca a polaco

#ingresar diccionario y asignar elemento a cada dato ingresado
numeros= { 'numeros':{'uno':'jeden', 'dos':'dwa', 'tres':'trzy', 'cuatro':'cztery', 'cinco':'piec','seis':'szesc', 'siete': 'siedem', 'ocho':'osiem', 'nueve': 'dziewiec', 'diez': 'dziesiec'}}

#ingresar datos que el usuario va a buscar
numerosbuscar1 = input ( 'ingresar 3 numeros del uno al diez en texto')
nombres= numerosbuscar1.split(',')


#mostrar en pantalla datos ingresados por el usuario
print (numeros['numeros'][nombres[0]])
print (numeros['numeros'][nombres[1]])
print (numeros['numeros'][nombres[2]])


