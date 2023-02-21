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
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp

### Typical module imports
import pandas as pd
import numpy as np
import os
#from functools import cache


###############NOTES#################
"""

    Must use FULLSCREEN for DataTable to select_all

"""
#####################################


### REMOVE LATER ###
Window.size = (940,600)
#Window.minimum_width, Window.minimum_height = Window.size
### ------------ ###




PRINCETON_ORANGE = (0.9 , 0.466 , 0.125 , 1)
EERIE_BLACK = (0.1 , 0.1 , 0.1 , 1)
BLOND = (1 , 0.96 , 0.698 , 1)
DARK_RED = (0.58 , 0.105 , 0.05 , 1)
BATTLESHIP_GREY = (0.518 , 0.55 , 0.555 , 1)



class CommonValues():
    chosen_rows = []
    df = pd.read_csv('data/data.csv')
    ingredients = [[str(x).title()] for x in df][1:]

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
    
    def add_table(self):
        if self.table_added: return

        self.choosing_table = MDDataTable(
                                        check=True,
                                        use_pagination=False,
                                        pagination_menu_pos='auto',
                                        background_color_header=BATTLESHIP_GREY,
                                        column_data=[('No.', dp(30)),('Toiduaine', dp(30)),('Sobivus', dp(30))],
                                        row_data=[*zip([*(range(1,len(CommonValues.ingredients)+1))],(x[0] for x in (CommonValues.ingredients)),[*(f"{round(x*100,1)}%" for x in list(CommonValues.df.mean(axis=0)))])],
                                        rows_num=len(CommonValues.ingredients)
                                        )
        
        self.ids.table_area.add_widget(self.choosing_table)
        self.ids['choosing'] = self.choosing_table
        self.ids.choosing.bind(on_check_press=self.update_chosen_rows)

        self.table_added = True

    def add_return_button(self, *_):

        # Add return button
        button = MDAnchorLayout(
                MDFillRoundFlatButton(
                    text='Kinnita',
                    font_size=30,
                    on_release=self.button_action
                    ),
                    anchor_x='right',
                    anchor_y='bottom',
                    padding=dp(20))
        self.add_widget(button)

    def update_chosen_rows(self, *_):
        CommonValues.chosen_rows = self.choosing_table.get_row_checks()
    
    def button_action(self, *_):
        self.parent.current = 'Calculation'
        self.update_chosen_rows()

class IngredientAmountChoosingScreen(MDScreen):
    past_ingredients = []


    def add_rows(self):
        
        # Clear children if values changed
        if self.past_ingredients != CommonValues.chosen_rows:
            self.ids.ingredient_list.clear_widgets(self.ids.ingredient_list.children)
        
        else:
            return
        
        self.past_ingredients = CommonValues.chosen_rows

        # Set new fields for input
        for item_name in self.past_ingredients:
            item_name = item_name[1]

            self.ids.ingredient_list.add_widget(MDLabel(
                text=item_name,
                font_size=50,
                size_hint=(1, None),
                text_color=EERIE_BLACK
            ))
            self.ids.ingredient_list.add_widget(MDTextField(
                input_filter='float',
                hint_text='Kogus grammides (nt. 38.6)',
                size_hint=(1, None),
                font_size=50
            ))


    def add_return_button(self, *_):
        
        # Add return button
        button = MDAnchorLayout(
                MDFillRoundFlatButton(
                    text='Kinnita',
                    font_size=30,
                    on_release=self.button_action
                    ),
                    anchor_x='right',
                    anchor_y='bottom',
                    padding=dp(20))
        self.add_widget(button)
    
    def button_action(self, *_):
        self.parent.current = 'Calculation'

class IngredientList(MDGridLayout):
    pass

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