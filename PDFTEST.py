from pdf2image import convert_from_path
from pathlib import Path
import pathlib

recipe_path = Path('data/recipes')

for file in recipe_path.iterdir():
    new_file_name = Path('data\\recipe_pics\\', str(file.name[:-4]) + '.jpg')
    image = convert_from_path(file, poppler_path='moledo-venv/poppler/Library/bin')
    image[0].save(new_file_name,'JPEG')
    

print(*(x.name[:-4] for x in recipe_path.iterdir()),sep='\n')