### Core and Tool imports
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.clipboard import Clipboard
from kivy.core.window import WindowBase, Window

### UI imports
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.properties import NumericProperty, AliasProperty
from kivy.metrics import dp
from kivy.config import Config
from kivymd.uix.dialog import MDDialog
from kivymd.uix.widget import MDWidget

### Typical module imports
import pandas as pd
import numpy as np
import os
from pathlib import Path
import random
from pdf2image import convert_from_path
#from functools import cache


##########     NOTES     ############
"""

    Must use FULLSCREEN for DataTable to select_all
    and back arrow to display correctly

"""
########## ------------- ############


##### SET WINDOW TO NON-RESIZEABLE #######

Window.maximize()
WindowBase.fullscreen = True

##### ---------------------------- #######


PRINCETON_ORANGE = (0.9 , 0.466 , 0.125 , 1)
EERIE_BLACK = (0.1 , 0.1 , 0.1 , 1)
BLOND = (1 , 0.96 , 0.698 , 1)
DARK_RED = (0.58 , 0.105 , 0.05 , 1)
BATTLESHIP_GREY = (0.518 , 0.55 , 0.555 , 1)



class CommonLogic():
    chosen_rows = []
    df = pd.read_csv('data/data.csv')
    ingredients = [[str(x).title()] for x in df][1:]
    calculation_errors = 0

    ingredient_amounts = {}

    def test(*a, **kw):
        print((a, kw) if a or kw else 'test')
    
    def update_ingredient_amount(text_field, *args, **kwargs):
        CommonLogic.ingredient_amounts[text_field.itemid] = text_field.text
    
    def calculate_suitability(*args, **kwargs) -> float:
        CommonLogic.calculation_errors = 0

        total_mass = sum([float(x) for x in CommonLogic.ingredient_amounts.values() if x != ''])
        total_suitable = 0.0

        for ingredient in CommonLogic.df[1:]:
            if ingredient.title() in CommonLogic.ingredient_amounts.keys():
                acceptances = CommonLogic.df[ingredient]
                try:
                    total_suitable += sum(acceptances)/len(acceptances)*(float(CommonLogic.ingredient_amounts[ingredient.title()])/total_mass)
                except:
                    CommonLogic.calculation_errors += 1

        return total_suitable
    
    def view_recipe(recipe:MDRectangleFlatButton):
        filename = recipe.text
        pic_exists = Path('data', 'recipe_pics', filename + '.jpg').exists()
        new_file_loc = Path('data', 'recipe_pics', filename + '.jpg')
        
        if not pic_exists:
            old_file_loc = Path('data', 'recipes', filename + '.pdf')

            image = convert_from_path(old_file_loc, poppler_path='moledo-venv/poppler/Library/bin')
            image[0].save(new_file_loc,'JPEG')
        
        RecipePicView.change_pic(filename, str(new_file_loc), recipe)

class CenterLayout(MDAnchorLayout):
    MDAnchorLayout.anchor_x = 'center'
    MDAnchorLayout.anchor_y = 'center'
    
class MainScreen(MDScreen):
    pass

class RecipeScreen(MDScreen):
    pass

class SuitabilityScreen(MDScreen):
    
    def show_result_dialog(*args, **kwargs):
        dialog = MDDialog(
            title=f"{round(CommonLogic.calculate_suitability()*100,1)}%",
            buttons=[
                MDFlatButton(
                    text="Sulge"
                ),
            ],
        )
        dialog.buttons[0].bind(on_release=dialog.dismiss)
        dialog.open()

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
                                        row_data=[*zip([*(range(1,len(CommonLogic.ingredients)+1))],(x[0] for x in (CommonLogic.ingredients)),[*(f"{round(np.mean(x)*100,1)}%" for x in [*(CommonLogic.df[x] for x in CommonLogic.df.columns[1:])])])],
                                        rows_num=len(CommonLogic.ingredients)
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
                    font_size=70,
                    md_bg_color=DARK_RED,
                    on_release=self.button_action
                    ),
                    anchor_x='right',
                    anchor_y='bottom',
                    padding=dp(20))
        self.add_widget(button)

    def update_chosen_rows(self, *_):
        CommonLogic.chosen_rows = self.choosing_table.get_row_checks()
    
    def button_action(self, *_):
        self.parent.current = 'Suitability'
        self.update_chosen_rows()

class IngredientAmountChoosingScreen(MDScreen):
    past_ingredients = []


    def add_rows(self):
        
        # Clear children if values changed
        if self.past_ingredients != CommonLogic.chosen_rows:
            self.ids.ingredient_list.clear_widgets(self.ids.ingredient_list.children)
        
        else:
            return
        
        self.past_ingredients = CommonLogic.chosen_rows

        # Set new fields for input
        for item_name in self.past_ingredients:
            item_name = item_name[1]

            self.ids.ingredient_list.add_widget(MDLabel(
                text=item_name,
                font_style='H2',
                size_hint=(1, None),
                text_color=EERIE_BLACK,
                halign='right',
                padding=(50, 0)
            ))
            text_field = MDTextField(
                input_filter='float',
                hint_text='Kogus grammides',
                size_hint=(1, None),
                font_size=40)
            text_field.itemid=item_name
            text_field.bind(focus=CommonLogic.update_ingredient_amount)
            self.ids.ingredient_list.add_widget(text_field)


    def add_return_button(self, *_):
        
        # Add return button
        button = MDAnchorLayout(
                MDFillRoundFlatButton(
                    text='Kinnita',
                    font_size=70,
                    md_bg_color=DARK_RED,
                    on_release=self.button_action
                    ),
                    anchor_x='right',
                    anchor_y='bottom',
                    padding=dp(20))
        self.add_widget(button)
    
    def button_action(self, *_):
        self.parent.current = 'Suitability'

class IngredientList(MDGridLayout):
    pass

class RecipeList(MDGridLayout):
    recipes = [x.name[:-4] for x in Path('data/recipes').iterdir()]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for recipe in self.recipes:
            self.add_widget(MDRectangleFlatButton(  text=recipe,
                                                    size_hint=(1, None),
                                                    font_size=50,
                                                    md_bg_color=BATTLESHIP_GREY,
                                                    line_color=EERIE_BLACK,
                                                    text_color=EERIE_BLACK,
                                                    on_release=CommonLogic.view_recipe
                                                ))

class RecipePicView(MDScreen):

    @classmethod
    def change_pic(self, recipe_name, image_location, widget):
        self.recipe_name = recipe_name
        self.image_location = image_location
        
        widget.parent.parent.parent.parent.parent.parent.current = 'Recipe View'

class MyScreenManager(MDScreenManager):
    pass

class MoledoApp(MDApp):
    pass


if __name__ == '__main__':
    MoledoApp().run()