#comtecdev
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from time import ctime
import webbrowser
from gtts import gTTS
import os
import random
import playsound
import pyaudio
import json
import weathercom
import translate
from translate import Translator
r=sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        print(1111)
        audio=r.listen(source)
        voice_data = r.recognize_google(audio, language='fr')
        print(voice_data)
        voice_data =''
        try:
            #voice_data=r.recognize_google(audio,language='fr')
            if not combo.get():
                juvenal_speak("Veuillez sèlectionner une langue d'abords")
            voice_data = r.recognize_google(audio, language=combo.get())
            st.text.insert(END, voice_data, "cible")
        except sr.UnknownValueError:
            juvenal_speak("Je vous reçois très faiblement veUillez reprendre s'il vous plait")
        except sr.RequestError:
            juvenal_speak('Désolé vérifier votre connexion')
    return voice_data

class ScrolledText(Frame):
    """Widget composite, associant un widget Text et une barre de défilement"""
    def __init__(self, boss, baseFont ="Times", widt =50, height =25):
        Frame.__init__(self, boss, bd =2, relief =SUNKEN)
        self.text =Text(self, font =baseFont, bg ='ivory', bd =1,width =widt, height =height)
        scroll =Scrollbar(self, bd =1, command =self.text.yview)
        self.text.configure(yscrollcommand =scroll.set)
        self.text.pack(side =LEFT, expand =YES, fill =BOTH, padx =2, pady =2)
        scroll.pack(side =RIGHT, expand =NO, fill =Y, padx =2, pady =2)

class ComboFull(Frame):
    "Widget composite associant un champ d'entrée avec une boîte de liste"
    def __init__(self, boss, item='', items=[]):
        Frame.__init__(self, boss)  # constructeur de la classe parente
        self.boss = boss    # référence du widget 'maître'
        self.items = items  # items à placer dans la boîte de liste
        self.item = item    # item entré ou sélectionné
        self.listSize = 10    # nombre d'items visibles dans la liste
        self.width = 15  # largeur du champ d'entrée (en caract.)
        self.entree = Entry(self, width=20)
        self.entree.insert(END, item)
        self.entree.bind("<Return>", self.sortieL)
        Button(self,text="↓↓", width=2,command=self.popup).grid(row=0,rowspan=1,column=2)
        Label(self, text='Langue! ', fg='black').grid(row=0,column=0)
        self.entree.grid(row=0,column=1,rowspan=1)
        self.gif1 = PhotoImage(file="ca.png")
        Button(self,activebackground="black",activeforeground="black" ,image=self.gif1, width=500, height=500,command=main).grid(row=2,rowspan=10,column=5,columnspan=15)

    def sortieL(self, event=None):
        index = self.bListe.curselection()
        ind0 = int(index[0])
        self.item = self.items[ind0]
        self.item =self.item[:2]
        print(self.item)
        self.entree.delete(0, END)
        self.entree.insert(END, self.item)
        self.pop.destroy()  # supprimer la fenêtre satellite

    def get(self):
        # Renvoyer le dernier item sélectionné dans la boîte de liste
        return self.item

    def popup(self):
        xW, yW = self.winfo_x(), self.winfo_y()
        geo = self.boss.geometry().split("+")
        xF, yF = int(geo[1]), int(geo[2])
        xP, yP = xF + xW + 10, yF + yW + 45 # +45 : compenser haut champ Entry
        self.pop = Toplevel(self)   # fenêtre secondaire ("pop up")
        self.pop.geometry("+{}+{}".format(xP, yP))  # positionnement / écran
        self.pop.overrideredirect(1)    # => fen. sans bordure ni bandeau
        self.pop.transient(self.master) # => fen. 'modale'
        cadreLB = Frame(self.pop)   # cadre pour l'ensemble des 2
        self.bListe = Listbox(cadreLB, height=self.listSize, width=self.width - 1)
        scrol = Scrollbar(cadreLB, command=self.bListe.yview)
        self.bListe.config(yscrollcommand=scrol.set)
        self.bListe.bind("<ButtonRelease-1>", self.sortieL)
        self.bListe.grid(row=3,rowspan=1,column=2,columnspan=1)
        scrol.grid(rowspan=5,columnspan=1)
        #scrol.pack(expand=YES, fill=Y)
        cadreLB.grid(row=1,rowspan=1,column=0,columnspan=1)
        # Remplissage de la boîte de liste avec les items fournis :
        for it in self.items:
            self.bListe.insert(END, it)

class ComboFull1(Frame):
    "Widget composite associant un champ d'entrée avec une boîte de liste"
    def __init__(self, boss, item='', items=[]):
        Frame.__init__(self, boss)  # constructeur de la classe parente
        self.boss = boss    # référence du widget 'maître'
        self.items = items  # items à placer dans la boîte de liste
        self.item = item    # item entré ou sélectionné
        self.listSize = 10    # nombre d'items visibles dans la liste
        self.width = 15  # largeur du champ d'entrée (en caract.)
        self.entree = Entry(self, width=20)
        self.entree.insert(END, item)
        self.entree.bind("<Return>", self.sortieL)
        Button(self,text="↓↓", width=2,command=self.popup).grid(row=0,rowspan=1,column=1)
        self.entree.grid(row=0,rowspan=1)
        self.gif1 = PhotoImage(file="ca.png")
    def sortieL(self, event=None):
        index = self.bListe.curselection()
        ind0 = int(index[0])
        self.item = self.items[ind0]
        self.item =self.item[:2]
        print(self.item)
        self.entree.delete(0, END)
        self.entree.insert(END, self.item)
        self.pop.destroy()  # supprimer la fenêtre satellite

    def get(self):
        # Renvoyer le dernier item sélectionné dans la boîte de liste
        return self.item

    def popup(self):
        xW, yW = self.winfo_x(), self.winfo_y()
        geo = self.boss.geometry().split("+")
        xF, yF = int(geo[1]), int(geo[2])
        xP, yP = xF + xW + 10, yF + yW + 45 # +45 : compenser haut champ Entry
        self.pop = Toplevel(self)   # fenêtre secondaire ("pop up")
        self.pop.geometry("+{}+{}".format(xP, yP))  # positionnement / écran
        self.pop.overrideredirect(1)    # => fen. sans bordure ni bandeau
        self.pop.transient(self.master) # => fen. 'modale'
        cadreLB = Frame(self.pop)   # cadre pour l'ensemble des 2
        self.bListe = Listbox(cadreLB, height=self.listSize, width=self.width - 1)
        scrol = Scrollbar(cadreLB, command=self.bListe.yview)
        self.bListe.config(yscrollcommand=scrol.set)
        self.bListe.bind("<ButtonRelease-1>", self.sortieL)
        self.bListe.grid(row=3,rowspan=1,column=2,columnspan=1)
        scrol.grid(rowspan=5,columnspan=1)
        #scrol.pack(expand=YES, fill=Y)
        cadreLB.grid(row=1,rowspan=1,column=0,columnspan=1)
        # Remplissage de la boîte de liste avec les items fournis :
        for it in self.items:
            self.bListe.insert(END, it)

def chercheCible(event=None):
    "défilement du texte jusqu'à la balise <cible>, grâce à la méthode see()"
    index = st.text.tag_nextrange('cible', '0.0', END)
    st.text.see(index[0])


def juvenal_speak(audio_string):
    #translator = Translator(to_lang=str(combo.get()))
    #translation = translator.translate(audio_string)
    tts=gTTS(text=audio_string, lang=str(combo.get()))
    r=random.randint(1,10000000)
    audio_file='audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    st.text.insert(END, audio_string, "cible")
    os.remove(audio_file)
def traduireDoc(doc):
    doc=doc + '.txt'
    f=open(doc,'r')
    if f.mode == 'r':
        cont=f.read()
        juvenal_speak('Voici le contenu initiale du document')
        st.text.insert(END, cont, "cible")
        translator = Translator(to_lang=str(combo2.get()))
        translation = translator.translate(cont)
        st.text.insert(END, translation, "cible")
        juvenal_speak('Ensuite voici la traduction du document,'+ translation)

def traduiretext(cont):
    translator = Translator(to_lang=str(combo2.get()))
    translation = translator.translate(cont)
    st.text.insert(END, translation, "cible")
    juvenal_speak('Voici la traduction de ce que vous venez de dire,' + translation)

def respond(voice_data):
    if "Bonjour" in voice_data:
        juvenal_speak("Bonjour utilisateur Je m'appeelle robot, j'ai été créé par juvénal Etudiant en Mathématiques et Informatique à la Faculté de Natitingou")
    if 'date' in voice_data:
        juvenal_speak(ctime())
    if 'recherche' in voice_data:
        juvenal_speak('Que voulez-vous recherchez?')
        search = record_audio()
        url='http://google.com/search?q='+ search
        webbrowser.get().open(url)
        juvenal_speak('Voici votre recherche de,' + search)
    if 'localise' in voice_data:
        #location = record_audio()
        #url='http://google.nl/maps/place/' + location + '&amp;'
        url = 'http://google.nl/maps/place/' + '&amp;'
        juvenal_speak('Voici votre localisation')
        webbrowser.get().open(url)
    if "météo" in voice_data:
        juvenal_speak('De quelle ville?')
        city = record_audio()
        weatherDetail = weathercom.getCityWeatherDetails(city)
        juvenal_speak(weatherDetail)
    if 'traduire' and 'parole' in voice_data:
        juvenal_speak('Quelle parole voulez-vous traduire?')
        cont = record_audio()
        traduiretext(cont)
    if 'document' in voice_data:
        juvenal_speak('Quel est le nom du document?')
        nom = record_audio()
        traduireDoc(nom)
    if 'bye' in voice_data:
        juvenal_speak("Ok bye ce fut un plaisir, A bientot")
        exit()
def main():
    juvenal_speak('Bonjour chers utilisateur, Que puis-je pour vous?')
    while 1:
        voice_data=record_audio()
        respond(voice_data)
if __name__ == '__main__':
    lang=['af(afrikaans)', 'ar(arabic)','nl(dutch)', 'en(english)', 'fr(french)', 'it(italian)', 'ja(japanese)','la(latin)','mg(malagasy)','pt(portuguese)','ru(russian)','so(somali)', 'es(spanish)']
    fen = Tk()
    fen.title("3V-vocal vivi (Assistance Vocale)")
    Label(fen, text='Destination de la Traduction! ', fg='black').pack()
    combo2 = ComboFull1(fen, item="", items=lang)
    combo2.pack()
    combo = ComboFull(fen, item="", items=lang)
    combo.pack()
    st = ScrolledText(fen, baseFont="Helvetica 12 normal", height=10)
    st.pack(expand=YES, fill=BOTH, padx=8, pady=8)
    st.text.tag_configure("Text", foreground="black",font="Helvetica 11 bold italic")
    st.text.tag_bind("lien", "<Button-3>", chercheCible)
    fen.mainloop()

