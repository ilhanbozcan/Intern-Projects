from kivy.app import App
from KivyProjects.todolist.SM import SM
from KivyProjects.todolist.screen.screen1 import screen1
from kivy.lang import Builder

Builder.load_file("screen/screen1.kv")
Builder.load_file("SM/SM.kv")

class main(App):
    def build(self):
        return SM.SM()


if __name__ == '__main__':
    main().run()

