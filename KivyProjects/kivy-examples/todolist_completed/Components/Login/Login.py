from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import sqlite3
from kivy.clock import Clock

con = sqlite3.connect("C:\\Users\\ilhan\\OneDrive\\Masaüstü\\todolist_deneme\\DB.db")
cursor = con.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS Accounts(username TEXT,password TEXT,account_id INTEGER PRIMARY KEY)")


con.commit()


class Login(Screen):

    def __init__(self,**kwargs):
        super(Login,self).__init__(**kwargs)

    def change_to_home(self,*args):
        self.manager.current = "Home"
        self.ids.info.text= ""
    def sign_in(self):
        uname = self.ids.uname.text
        pwd = self.ids.pwd.text

        info = self.ids.info
        database = con.execute("SELECT * FROM Accounts")



        if uname == "" or pwd == "":
            info.text= "[color=#FF0000]username or password required[/color]" #red
        else:
            for row in database:

                if uname == row[0] and pwd == row[1]:
                    info.text = "[color=#00FF00] Logged In Successfully[/color]" #green
                    self.manager.uname = row[0]
                    self.manager.pwd = row[1]
                    self.manager.user_id = row[2]


                    Clock.schedule_once(self.change_to_home, 2)

                    break

                else:
                    info.text = "[color=#FF0000]Invalid username or password[/color]"  # red
    def sign_up(self):
        database = con.execute("SELECT username,password FROM Tablo2")






