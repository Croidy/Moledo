from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
import pandas as pd



class MainScreen(Screen):
    pass

class OtherScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass


class MoledoApp(App):
    pass



if __name__ == '__main__':
    MoledoApp().run()