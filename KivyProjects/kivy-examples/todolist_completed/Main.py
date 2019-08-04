from kivy.app import App

from kivy.lang.builder import Builder
from Components.Home.Home import Home
from Components.SM.SM import SM
from Components.SignUp.SignUp import SignUp
from Components.Login.Login import Login
Builder.load_file("Components/SM/SM.kv")
Builder.load_file("Components/Home/Home.kv")
Builder.load_file("Components/Login/Login.kv")
Builder.load_file("Components/SignUp/SignUp.kv")



class Main(App):
    def build(self):

        return SM()


if  __name__ == "__main__":
    Main().run()


