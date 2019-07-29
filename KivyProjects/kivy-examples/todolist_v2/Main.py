from kivy.app import App

from kivy.lang.builder import Builder
from Components.Home.Home import Home
from Components.SM.SM import SM
Builder.load_file("Components/Home/Home.kv")
Builder.load_file("Components/SM/SM.kv")



class Main(App):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
    
    def build(self):

        return SM()


if  __name__ == "__main__":
    Main().run()


