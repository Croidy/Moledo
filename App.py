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
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.metrics import dp

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
    MDAnchorLayout.anchor_x = 'center'
    MDAnchorLayout.anchor_y = 'center'
    

class MainScreen(MDScreen):
    pass

class RecipeScreen(MDScreen):
    pass

class CalculationScreen(MDScreen):
    pass

class IngredientChoosingScreen(MDScreen):
    table_added = False
    chosen_rows = []
    
    def add_table(self):
        if self.table_added: return

        self.choosing_table = MDDataTable(
                                        check=True,
                                        use_pagination=False,
                                        background_color_header=BATTLESHIP_GREY,
                                        column_data=[('No.', dp(30)),
                                                     ('Toiduaine', dp(30))],
                                        row_data=[['1','Porgand'],['2','Kurk'],['3','Tomat']]
                                        )
        
        self.add_widget(self.choosing_table)
        self.ids['choosing'] = self.choosing_table
        self.ids.choosing.bind(on_check_press=self.update_amount_table)

        self.table_added = True

        button = MDAnchorLayout(
                MDFillRoundFlatButton(
                    text='Kinnita',
                    font_size=30,
                    on_release=self.button_action
                    ),
                    anchor_x='right',
                    anchor_y='bottom',
                    padding=dp(10))
        self.add_widget(button)

    def update_amount_table(self, *_):
        self.chosen_rows = self.choosing_table.get_row_checks()
    
    def button_action(self, *_):
        self.parent.current = 'Calculation'
    
    @classmethod
    def get_chosen_rows(self):
        return self.chosen_rows

class IngredientAmountChoosingScreen(MDScreen):

    def add_rows(self):
        
        print(IngredientChoosingScreen.get_chosen_rows())

        button = MDAnchorLayout(
                MDFillRoundFlatButton(
                    text='Kinnita',
                    font_size=30,
                    on_release=self.button_action
                    ),
                    anchor_x='right',
                    anchor_y='bottom',
                    padding=dp(10))
        self.add_widget(button)
    
    def button_action(self, *_):
        self.parent.current = 'Calculation'

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