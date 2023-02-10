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
    pass



class MainScreen(MDScreen):
    pass



class RecipeScreen(MDScreen):
    pass



class CalculationScreen(MDScreen):
    table_added = False



    def add_tables(self):
        if self.table_added: return

        ########   DATATABLES   #########
        self.choosing_table = MDDataTable(
                                    check=True,
                                    use_pagination=False,
                                    background_color_header=PRINCETON_ORANGE,
                                    background_color_selected_cell=DARK_RED,
                                    background_color_cell=BLOND,
                                    column_data=[('No.', dp(30)),
                                                 ('Toiduaine', dp(30))],
                                    row_data=[['1','Porgand'],['2','Kurk'],['3','Tomat']]
                                    )

        self.amount_table = MDDataTable(
                                    check=True,
                                    use_pagination=False,
                                    background_color_header=PRINCETON_ORANGE,
                                    background_color_selected_cell=DARK_RED,
                                    background_color_cell=BLOND,
                                    column_data=[('No.', dp(30)),
                                                 ('Toiduaine', dp(30))],
                                    row_data=[['1','Porgand'],['2','Kurk'],['3','Tomat']]
                                    )
        ######## ------------- #########


        self.ids.table_area.add_widget(self.choosing_table)
        self.ids['choosing'] = self.choosing_table
        self.ids.choosing.bind(on_check_press=self.update_amount_table)
        self.ids.table_area.add_widget(self.amount_table)
        self.ids['amount'] = self.amount_table

        self.table_added = True
    
    def update_amount_table(self, *_):
        print(self.choosing_table.get_row_checks())




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