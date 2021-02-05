import vlc
import time
import glob

#instancia del reproductor
vlc_instance = vlc.Instance()
player = vlc_instance.media_list_player_new()#funcion para hacer slideshow



def reproducirUSB():
	#se guardan los nombres de los archivos tipo png en una lista
	varPhotoFiles = glob.glob("Fotos/*.png")#En carpeta fotos
	#se guardan los nombres de los archivos tipo mp4 en una lista
	varVideoFiles = glob.glob("Videos/*.mp4")#EN carpeta videos
	#se guardan los nombres de los archivos tipo mp3 en una lista
	varMusicFiles = glob.glob("Musica/*.mp3")#EN carpeta musica
	
	if (varPhotoFiles and varVideoFiles) or (varPhotoFiles and varMusicFiles) or (varVideoFiles and varMusicFiles) :
		print("Elige que reproducir:\n1.-Fotos\n2.-Videos\n3.-Musica")
		opcionReproduccion = input()		
		if opcionReproduccion == '1':
			mymedia = varPhotoFiles
			tiempoReproduccion = 4 #tiempo que cada slide está en pantalla
		elif opcionReproduccion == '2':
			mymedia = varVideoFiles
			tiempoReproduccion = 33 #ajustar para cada video	
		elif opcionReproduccion == '3':
			mymedia = varMusicFiles
			tiempoReproduccion = 33 #ajustar para cada cancion	
	elif not varVideoFiles and not varMusicFiles:#si no hay archivos de video se cargan fotos
	    mymedia = varPhotoFiles
	    tiempoReproduccion = 4 #tiempo que cada slide está en pantalla
	elif not varPhotoFiles and not varMusicFiles:#si no hay archivos de fotos ni musica se cargan videos
	    mymedia = varVideoFiles
	    tiempoReproduccion = 33 #ajustar para cada video
	elif not varPhotoFiles and not varVideoFiles:#si no hay archivos de fotos ni musica se cargan videos
	    mymedia = varMusicFiles
	    tiempoReproduccion = 33 #ajustar para cada video

	Media = vlc_instance.media_list_new(mymedia)
	player.set_media_list(Media)

	#cada elemento de la lista se reproduce en pantalla por 4 segundos
	for index, name in enumerate(mymedia):
	    player.play_item_at_index(index)
	    time.sleep(tiempoReproduccion)#el tiempo de reproduccion de las fotos, videos o musica
	Media.close()#IMPORTANTE, debe cerrarse el reproductor

print("1.- Ver servicio de video online(Netlfix). \n2.- Reproducir musica(Spotify). \n3.- Reproducir contenido en USB")
opcion = input()
if opcion == '3':
	reproducirUSB()
else:
	print("Reproduciendo Netlfix o Spotify")
	print(opcion)



#Comentario