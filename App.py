from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import NumericProperty
from kivy.lang import Builder       #Not Used
from kivy.clock import Clock        #Not Used

from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

import pandas as pd
import numpy as np
import os
#from functools import cache


class MainScreen(Screen):
    pass

class RecipeScreen(Screen):
    pass


class RecipeScrollView(ScrollView):
    recipes = os.listdir("data/recipes")
    list_size = NumericProperty(len(recipes))
       
class RecipeList(GridLayout):
    recipes = os.listdir("data/recipes")
    list_size = NumericProperty(len(recipes))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for recipe in RecipeScrollView.recipes:
            self.add_widget(Button(text=recipe[:-4],size_hint_y=None,font_size=50))


class MyScreenManager(ScreenManager):
    pass


class MoledoApp(App):
    RecipeScrollView = RecipeScrollView()



if __name__ == '__main__':
    MoledoApp().run()