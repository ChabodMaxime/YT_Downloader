from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import os


def getit():

    video_link = entree.get()
    video = YouTube(video_link)
  
    audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
    result = audio.download()
    path = os.path.dirname(__file__)
    taille_path = len(path)
    name_video = result[taille_path+1:-4]
    os.rename(name_video + '.mp4', name_video + '.mp3')
    messagebox.showinfo("Info", "Nom de la musique télécharger: " + name_video + ".mp3")
 

window = Tk()
window.geometry("400x150")

label = Label(window, text="Entrez l'url de la video youtube")
label.pack()

value = StringVar() 
value.set("Ex: https://www.youtube.com/watch?v=Aqb7aD4OEwM")
entree = Entry(window, textvariable=str, width=30)
entree.insert(0, "Ex: https://www.youtube.com/watch?v=Aqb7aD4OEwM")
entree.pack()
Button(window, text ='Télécharger', command=getit).pack(side=TOP, padx=5, pady=5)

window.mainloop()
