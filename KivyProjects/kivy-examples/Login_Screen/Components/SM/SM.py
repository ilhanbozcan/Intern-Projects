from kivy.uix.screenmanager import ScreenManager
from Components.Login.Login import Login


class SM(ScreenManager):

    def __init__(self, **kwargs):
        super(SM, self).__init__(**kwargs)
        self.current = "Login"
