from kivy.uix.screenmanager import Screen
import sqlite3
from kivy.clock import Clock

con = sqlite3.connect("C:\\Users\\ilhan\\OneDrive\\Masaüstü\\todolist_deneme\\DB.db")
cursor = con.cursor()
con.commit()





class SignUp(Screen):

    def __init__(self,**kwargs):
        super(SignUp,self).__init__(**kwargs)

    def change_to_login(self,*args):
        self.manager.current = "Login"

    def sign_up(self):
        username = self.ids.uname.text
        password = self.ids.pwd.text
        info = self.ids.info

        info.text = "[color=#00FF00]Created[/color]"
        cursor.execute("INSERT INTO Accounts (username,password) VALUES(?,?)",
                       (username,password,))
        con.commit()

        Clock.schedule_once(self.change_to_login,2)



