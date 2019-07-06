from kivy.app import App
from kivy.lang import Builder

from KivyProjects.kivyExample.SM import SM
from KivyProjects.kivyExample.Screen1.Screen1 import Screen1

Builder.load_file("Screen1/Screen1.kv")
Builder.load_file("SM/SM.kv")

class main(App):
    def build(self):
        return SM.SM()


if __name__ == '__main__':
    main().run()

