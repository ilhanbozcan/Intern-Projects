from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder
from Components.SM import SM




class Home(Screen):
    def __init__(self,**kwargs):
        super(Home,self).__init__(**kwargs)

        EachTask.RemoveWidget = self.removeWidget

        """
        for task in tasks:
            self.ids.add_field(Home.EachTask(text=task))
        """

    def removeWidget(self,instance):
        children = self.ids.add_field.children
        self.ids.add_field.remove_widget(self.ids.add_field.ids[instance.parent.id])

        print(self.ids.add_field.children)
        #self.ids.add_field.clear_widgets()
        #for child in children:
            #self.ids.add_field.add_widget(child)

        #print(instance.)
        #self.remove_widget(instance.parent)
        #self.clear_widgets()


    def addWidget(self):
        input = self.ids.input.text
        newListItem = EachTask(text=input, id=str((len(self.ids.add_field.children))) )
        print(newListItem.id)
        self.ids.add_field.add_widget(newListItem)
        print(self.ids.add_field.children)






class EachTask(BoxLayout):
    def __init__(self, text= "", **kwargs):
        super(EachTask,self).__init__(**kwargs)
        self.ids.label.text = text


    def RemoveWidget(self,instance):
        pass

















