from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

import pandas as pd
import numpy as np
import os
#from functools import cache


class MainScreen(Screen):
    pass

class RecipeScreen(Screen):
    pass


class RecipeScrollView(ScrollView):
    
    def get_recipes(self):
        view = self.parent.parent.ids['recipe_scrollview']
        view.add_widget(Label(text='hello', font_size=50, size_hint_y=None, height=50))
       



class MyScreenManager(ScreenManager):
    pass


class MoledoApp(App):
    RecipeScreen = RecipeScreen()



if __name__ == '__main__':
    MoledoApp().run()