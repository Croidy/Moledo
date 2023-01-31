### Core and Tool imports
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window

### UI imports
from kivymd.uix.button.button import MDRectangleFlatButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.anchorlayout import MDAnchorLayout

### Typical module imports
import pandas as pd
import numpy as np
import os
#from functools import cache

### REMOVE LATER ###
Window.size = (940,600)
#Window.minimum_width, Window.minimum_height = Window.size
### ------------ ###

PRINCETON_ORANGE = (0.9 , 0.466 , 0.125 , 1)
EERIE_BLACK = (0.1 , 0.1 , 0.1 , 1)
BLOND = (1 , 0.96 , 0.698 , 1)
DARK_RED = (0.58 , 0.105 , 0.05 , 1)
BATTLESHIP_GREY = (0.518 , 0.55 , 0.555 , 1)



class CenterLayout(MDAnchorLayout):
    pass


class MainScreen(MDScreen):
    pass

class RecipeScreen(MDScreen):
    pass

class CalculationScreen(MDScreen):
    df: pd.DataFrame = pd.read_csv('data/data.csv')
    
    def calc(self, feature):
        print(self.df[[feature]])

class RecipeScrollView(MDScrollView):
    recipes = os.listdir("data/recipes")
    list_size = len(recipes)
       
class RecipeList(MDGridLayout):
    recipes = os.listdir("data/recipes")
    list_size = len(recipes)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for recipe in RecipeScrollView.recipes:
            self.add_widget(MDRectangleFlatButton(  text=recipe[:-4],
                                                    size_hint=(1, None),
                                                    font_size=50,
                                                    md_bg_color=BATTLESHIP_GREY,
                                                    line_color=EERIE_BLACK,
                                                    text_color=EERIE_BLACK
                                                ))

class MyScreenManager(MDScreenManager):
    pass


class MoledoApp(MDApp):
    pass


if __name__ == '__main__':
    MoledoApp().run()