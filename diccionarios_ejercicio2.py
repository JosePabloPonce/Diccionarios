#Jose Pablo Ponce, 19092
#20-02-19
#diccionarios_ejercicio2
#Programa que al ingresar un dia, muestre la informacion correspondiente de la cancion

#diccionario con llaves y colecciones
dias = { 'informacion': {'lunes' : {'cancion':'Billie Jean', 'artista':'Michael Jackson', 'album':'Thriller', 'año': '1982'},
        'martes' : {'cancion':'I Wanna Dance With Somebody', 'artista':'Whitney Houston', 'album':'Whitney','año':'1987'},
        'miercoles' :{'cancion':'Comfortably numb', 'artista':'Pink Floyd', 'album':'The Wall', 'año': '1979'},
        'jueves' : {'cancion':'Yellow', 'artista':'Coldplay', 'album':'Yellow', 'año': '2000'},
        'viernes' :{'cancion':'Counting Stars', 'artista':'OneRepublic', 'album':'Native', 'año': '2013'},
        'sabado' :{'cancion':'Rolling in the Deep', 'artista':'Adele', 'album':'21', 'año': '2011'},
        'domingo' :{'cancion':'Living on a prayer', 'artista':'Bon Jovi', 'album':'Slippery When Wet', 'año':'1986'}
                    }}
#ingresar dia de la semana
canciondia = input ('ingresar dia')


#mostrar en pantalla imformacion del dia ingresado
print (dias['informacion'][canciondia])
print (" ")
print (" ")

#mostrar informacion del resto de dias de la semana
print (dias)


