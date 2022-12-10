import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.slider import Slider 
from kivy.uix.scrollview import ScrollView
from datetime import datetime
from kivy.core.text import LabelBase
from kivy.uix.spinner import Spinner
import random 
from kivy.uix.popup import Popup 
from kivy.uix.floatlayout import FloatLayout 


class MainWindow(Screen):
    def Feldeins(self): 
        pass

    def Feldzwei(self): 

        with open ("Unlocked" +'.txt', 'r') as m:
            Unlocked = m.read()

        if Unlocked == "True":
            self.parent.current = "FirstandahalfWindow"
        else:
            self.parent.current = "First"

    def Startsichtbar(self ):

        self.manager.get_screen("First").ids.start.opacity = 0
        self.manager.get_screen("First").ids.start.disabled = True 

            


    def Felddrei(self): 
        pass

    def Feldvier(self): 
        pass


    def kill(self): 
        self.nova.opacity = 0
    


class SecondWindow(Screen):

    global WichtigPunkte 
    global WartenPunkte 
    global ZuSpätPunkte 
    global WunschnachAnrufPunkte 
    global DenisZuSpätPunkte 
    global Allgemeinpunkte 

    def Deniswunsch(self): 
        self.denispunsch.text = str(random.randint(1,10))

    def Auswerten(self): 

        WichtigPunkte = 0 
        WartenPunkte = 0 
        ZuSpätPunkte = 0 
        WunschnachAnrufPunkte = 1 
        DenisZuSpätPunkte = 0 
        AllgemeinPunkte = 1 
        Antwortwahrscheinlichkeit = 10 


        if self.wichtig.active: 
            WichtigPunkte = 5

        if self.spaet.active: 
            ZuSpätPunkte = -2

        if self.warten.active: 
            WartenPunkte = -2 

        now = datetime.now()
        current_time = now.strftime("%H%M%S")

        if int(current_time) > 200000 < 230000: 
            DenisZuSpätPunkte = 2
            antwort = "Nö Zeitlich passt das"

        elif int(current_time) > 230000: 
            DenisZuSpätPunkte = -6
            antwort = "Ich habe gesagt 23 Uhr ist Schluss \n aber wenss sein muss -_- "
        
        elif int(current_time) < 80000: 
            DenisZuSpätPunkte = -9 
            antwort = "Mädchen bist du dumm ? geh pennen"

        elif int(current_time) < 140000: 
            DenisZuSpätPunkte = -2
            antwort = "Jetzt ist eher Ungünstig aber \n es hat dich eh noch nie aufgehalten"

        else: 
            DenisZuSpätPunkte = 0
            antwort = "hast du jetzt echt nichts besseres zutun ?"

        WunschnachAnrufPunkte = self.wiesehr.value 

        AllgemeinPunkte = WichtigPunkte + WartenPunkte + ZuSpätPunkte + WunschnachAnrufPunkte + DenisZuSpätPunkte


        Antwortwahrscheinlichkeit = (Antwortwahrscheinlichkeit + DenisZuSpätPunkte) * 10

        if Antwortwahrscheinlichkeit > 10: 
            Antwortwahrscheinlichkeit = 90 

        Antwortwahrscheinlichkeitstr = str(Antwortwahrscheinlichkeit) + "%"

        if AllgemeinPunkte >= 10: 
            Sollst = "Ja"
        elif AllgemeinPunkte < 10 and AllgemeinPunkte > 4: 
            Sollst = "wenns sein muss "
        else: 
            Sollst = "Nein"

        self.antwort.text = antwort
        self.solltestdu.text = "solltest du Denis Anrufen:   " + Sollst 
        self.antwortt.text = "Wahrscheinlichkeit dass Denis Antwortet:   " + Antwortwahrscheinlichkeitstr
        self.denispunsch.text = str(random.randint(0,4))

        print (AllgemeinPunkte)


        


        
        






    

class FirstWindow(Screen):

    def Emil(self): 
        global Name
        Name = "Emil"

    def Emily(self): 
        global Name
        Name = "Emily"

    def Nova(self): 
        global Name
        Name = "Nova"

    def Denis(self): 
        global Name
        Name = "Denis"

    def Jesus(self): 
        global Name
        Name = "Jesus"

    def Paul(self): 
        global Name
        Name = "Paul"

    def Marlene(self): 
        global Name
        Name = "Marlene"

    def Niemand(self): 
        global Name
        Name = "Niemand"


    def Checken(self):

        with open ("Unlocked" +'.txt', 'r') as m:
            Unlocked = m.read()

        if Unlocked != "True":

            with open ("Zitat" +'.txt', 'a') as m:
                pass

            with open ("Name" +'.txt', 'a') as m:
                pass

            with open ("Nummer" +'.txt', 'a') as m:
                pass


            with open ("Nummer" +'.txt', 'r') as m:
                Nummer = m.read()
                if int(Nummer) == 19: 
                    with open ("Unlocked" +'.txt', 'w') as m:
                        m.write("True")

                    Nummer = 0
                    print(Nummer)
                    self.spruch.text = "Jesus hält 6 Minuten"

                    with open ("Nummer" +'.txt', 'w') as m:
                        m.write(str(Nummer))

                    self.parent.current = "FirstandahalfWindow"
                    return 
            with open ("Zitat" +'.txt', 'r', encoding="utf-8") as m:
                list = m.read().splitlines()

                Spruch = list[int(Nummer)]
                AusgabeSpruch = list[int(Nummer)+1]

            with open ("Name" +'.txt', 'r') as m:
                list = m.read().splitlines()

                Person = list[int(Nummer)]

            if Person == Name: 
                self.spruch.text = AusgabeSpruch

                with open ("Nummer" +'.txt', 'w') as m:
                    Nummer = int(Nummer) + 1 
                    m.write(''.join([str(Nummer)]))

                    self.counter.text = (str(Nummer) + "/20")

            else:
                print(Person,Spruch,Name)

                with open ("Nummer" +'.txt', 'w') as m:
                    Nummer = 0
                    m.write(''.join([str(Nummer)]))

                self.parent.current = "main" 
                self.spruch.text = "Jesus hält 6 Minuten"

        else: 

            with open ("Zitat" +'.txt', 'r', encoding="utf-8") as m:
                list = m.read().splitlines()

            with open ("Name" +'.txt', 'r', encoding="utf-8") as m:
                listnamen = m.read().splitlines()

            Anzahlsprüche = -1
            for i in list:
                Anzahlsprüche = Anzahlsprüche + 1

            y = -1
            Unbenutzterindex = []

            for i in list:
                y = y + 1
                Unbenutzterindex.append(y)

            Fragespruch = random.randint(0,Anzahlsprüche)
            print(listnamen)
            Spruch = list[Fragespruch]
            global name 
            name = listnamen[Fragespruch]

            self.spruch.text = Spruch 

            print(name,Fragespruch,Spruch )


    def CheckifRichtig(self):
        

        with open ("Unlocked" +'.txt', 'r') as m:
            Unlocked = m.read()

        if Unlocked == "True":

            if Name == name:

                with open ("Nummer" +'.txt', 'r') as m:
                        Numerr = m.read()
                        Nummer = int(Numerr)


                if Nummer == 19: 
                    with open ("Nummer" +'.txt', 'w') as m:
                        Nummer = 0
                        m.write(''.join([str(Nummer)]))

                    self.parent.current = "FirstandahalfWindow"
                    self.showpop()

                else:
                    with open ("Nummer" +'.txt', 'w') as m:
                            Nummer = Nummer + 1 
                            m.write(''.join([str(Nummer)]))
                    self.counter.text = str(Nummer) + "/20"
            else: 
                with open ("Nummer" +'.txt', 'w') as m:
                    m.write("0")

                self.counter.text = "0/20"
                self.parent.current = "FirstandahalfWindow"
                self.start.opacity = 1
                self.start.disabled = False
        else: 
            pass
                

            
    def startt(self):

        self.start.opacity = 0
        self.start.disabled = True 
        global Name
        Name = ""
        self.counter.text = "0/20"

        with open ("Nummer" +'.txt', 'w') as m:
                    m.write("0")

            
    def showpop(self):
        show = P()
        global popupWindow
        popupWindow = Popup(title="Du hast es geschafft", content = show, size = (400,400))
        popupWindow.open()
            

class P(FloatLayout):

    def close(self):
        self.close_popup()

    def close_popup(self):
        popupWindow.dismiss()

    

class ThirdWindow(Screen):

    def Gems(self):
        global product
        product = self.gems.text 






    def buy(): 
        with open("Geld" + ".txt" , "r" , encoding="utf-8") as m: 
            Geld = int(m.read())


class FourthWindow(Screen):


    pass

class FirstandahalfWindow(Screen):

    def Hinzufuegen(self): 

        Zitat = self.willhinzufuegen.text
        Person = self.dername.text

        if Person != "Choose" and Zitat != "Zitat":

            with open("Zitat" + ".txt","a") as m: 
                m.write(''.join([str('"' + Zitat + '"') + "\n"]))


            Person = self.dername.text

            with open("Name" + ".txt" , "a") as m:
                m.write(''.join([str(Person) + "\n"]))

            self.willhinzufuegen.text = ""
        else: 
            pass


    def Darstellen(self):


        with open("Zitat" + ".txt" , "r" , encoding="utf-8") as m: 
            list = m.read().splitlines()


        for i in list: 
            Darstelltext = Darstelltext + i + "\n"
            self.ausgabe.text = Darstelltext


    def Sortieren(self): 

        with open("Name" + ".txt" , "r" , encoding="utf-8") as m:
            list = m.read().splitlines()

        value = self.dername.text

        y = -1
        Sortiertenamenindex = []
        print(list)

        for i in list:
            y = y + 1
            if i == value:
                Sortiertenamenindex.append(y)
                print(Sortiertenamenindex)
                print(value)

        with open("Zitat" + ".txt" , "r", encoding="utf-8") as m: 
            list = m.read().splitlines()

        sortedlist = [list[i] for i in Sortiertenamenindex]

        sortedprintreadylist = []
        for i in sortedlist:
            sortedprintreadylist.append(i + "\n")
            
        for i in sortedprintreadylist: 
            sortedprintreadylist2 = "".join(str(value +":    " + i + "\n") for i in sortedprintreadylist)

        if Sortiertenamenindex == []:
            sortedprintreadylist2 = "LEER"

        self.ausgabe.text = sortedprintreadylist2 

    def Checken():

        x = FirstWindow.Checken()

    def Gaming(self):

        self.parent.current = "First" 


    def Startsichtbar(self):
        self.manager.get_screen("First").ids.start.opacity = 1
        self.manager.get_screen("First").ids.start.disabled = False 

        
class WindowManager(ScreenManager):

    pass



class MyMainApp(App):
    def build(self):
        Window.clearcolor = (0.08,0.12,0.17,1)
        kv = Builder.load_file("my.kv")
        return kv
    def on_start(self, **kwargs):
        with open ("Nummer" +'.txt', 'r') as m:
            Nummer = m.read()
            if int(Nummer) != 19: 
                with open ("Nummer" +'.txt', 'w') as m:
                    Nummer = 0
                    m.write(''.join([str(Nummer)]))


if __name__ == "__main__":
    MyMainApp().run()