from kivy.uix.screenmanager import ScreenManager
from kivy.properties import NumericProperty
from kivy.properties import StringProperty

class SM(ScreenManager):
    user_id = NumericProperty()
    uname = StringProperty()
    pwd = StringProperty()
    def __init__(self, **kwargs):
        super(SM,self).__init__(**kwargs)
        self.current = "Login"


