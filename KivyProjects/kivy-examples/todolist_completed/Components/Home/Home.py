from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Components.Login.Login import Login


import time,datetime
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import sqlite3




con = sqlite3.connect("DB.db")
cursor = con.cursor()
default = False

cursor.execute("CREATE TABLE IF NOT EXISTS Tasks (task TEXT,time TEXT,control BOOLEAN,account_id TEXT,id INTEGER PRIMARY KEY)")




database = con.execute("SELECT * from Tasks")

class MyPopup(Popup):
    popup_id = StringProperty("")
    def __init__(self, **kwargs):
        super(MyPopup, self).__init__(**kwargs)




    def Remove_widget(self, instance):

        pass
    def Do_popup_task(self,instance):
        pass

class Home(Screen):
    uname = StringProperty()
    pwd = StringProperty()


    def __init__(self,**kwargs):
        super(Home,self).__init__(**kwargs)
        EachTask.Remove_widget = self.remove_widget
        MyPopup.Remove_widget = self.remove_widget_pop
        EachTask.Do_Popup_Task = self.do_popup_task
        Clock.schedule_interval(self.ClockFunction, 3)


    def on_enter(self, *args):




        Account_db = con.execute("SELECT * FROM Tasks WHERE account_id in(SELECT account_id FROM Accounts WHERE username= '"+ self.manager.uname +"' and password = '"+self.manager.pwd +"' )")



        for row in Account_db:


            if (row[2]) == True:
                newListItem = EachTask(rgba=[0, .7, .3, 1],
                                       text= row[0] + "    time:    " + row[1],
                                       id=str(row[4]))
                self.ids.add_field.add_widget(newListItem)

            else:

                    newListItem = EachTask(text=row[0] + "    time:    " + row[1],
                                           id=str(row[4]))

                    self.ids.add_field.add_widget(newListItem)
    def ClockFunction(self, *args):
        an = datetime.datetime.now()
        hour = an.hour
        min = an.minute
        if hour < 10:
            saat = "0" + str(hour)
        else:
            saat = str(hour)
        if min < 10:
            dak = "0" + str(min)
        else:
            dak = str(min)
        instant = saat + ":" + dak


        database_time = con.execute("SELECT * from Tasks")

        for row in database_time:
            if row[1] == instant and row[2] == 0:
                    """
                    the_popup = Popup(title="Time out", content= content, size_hint=(None, None),
                                      size=(500, 250)  )
                    the_popup.open()
                    """
                    self.the_popup = MyPopup()
                    self.the_popup.popup_id = str(row[4])

                    self.the_popup.open()
                    break




    def addWidget(self):

        task_input = self.ids.task_input.text
        time_input = self.ids.time_input.text
        cursor.execute("INSERT INTO Tasks(task,time,control,account_id) VALUES(?,?,?,?)", (task_input,time_input,default,self.manager.user_id))
        con.commit()
        id = con.execute("SELECT id FROM Tasks WHERE task ='"+task_input +"' and time= '"+time_input +"' and account_id = '"+str(self.manager.user_id )+"'" )
        id = id.fetchall()
        id = id [0][0]

        newListItem = EachTask(text= task_input + "    time:    " + time_input  , id=str(id))
        self.ids.add_field.add_widget(newListItem)



    def remove_widget(self, instance):


        self.ids.add_field.remove_widget(instance.parent.parent)
        cursor.execute("DELETE FROM Tasks WHERE id = '"+str(instance.parent.parent.id) +"'")
        con.commit()
        print("out")

    def remove_widget_pop(self,instance):
        print(self.the_popup.popup_id)

        for child in self.ids.add_field.children:
            if child.id == self.the_popup.popup_id:
                self.ids.add_field.remove_widget(child)
                cursor.execute("DELETE FROM Tasks WHERE id = '" + str(child.id) + "'")
                con.commit()

    def do_popup_task(self, instance):
        print("in")

        for child in self.ids.add_field.children:
            if child.id == self.the_popup.popup_id:
                if (child.rgba == [1, .5, .5, 1]):
                    child.rgba = [0, .7, .3, 1]
                    cursor.execute("UPDATE Tasks SET control = 1 WHERE id IN (SELECT id from Tasks  WHERE id = '" + child.id + "')")
                    con.commit()

                else:
                    child.rgba = [1, .5, .5, 1]
                    cursor.execute(
                        "UPDATE Tasks SET control = 0 WHERE id IN(SELECT id from Tasks  WHERE id = '" +child.id + "')")
                    con.commit()


class EachTask(BoxLayout):

    rgba = ListProperty([1, .5, .5, 1])
    def __init__(self, text= "", **kwargs):

        super(EachTask,self).__init__(**kwargs)
        input = self.ids.input.text
        time_input = self.ids.time_input.text
        id = con.execute("SELECT id FROM Tasks WHERE task ='" + input + "' and time= '" + time_input + "'")




        newListItem = EachTask(text=input, id=str(id))
        self.ids.add_field.add_widget(newListItem)
        MyPopup.Do_popup_task =self.Do_Popup_Task



    def __init__(self, text="", **kwargs):
        super(EachTask, self).__init__(**kwargs)
        self.ids.label.text = text
        MyPopup.Do_popup_task = self.Do_Popup_Task


    def Do_Task(self,instance):



        id = str(instance.parent.parent.id)
        print(id)


        if (self.rgba == [1, .5, .5, 1]):
            self.rgba = [0,.7,.3,1]
            cursor.execute("UPDATE Tasks SET control = 1 WHERE id IN (SELECT id from Tasks  WHERE id = '" + id + "')")
            con.commit()

        else:
            self.rgba = [1, .5, .5, 1]
            cursor.execute("UPDATE Tasks SET control = 0 WHERE id IN(SELECT id from Tasks  WHERE id = '" + id + "')")
            con.commit()




    def Remove_widget(self, instance):
       pass


    def Do_Popup_Task(self,instance):
        pass













