from pdf2image import convert_from_path
import pathlib

"""
p = pathlib.Path('data/recipes')

for file in p.iterdir():
    images = convert_from_path(file, poppler_path='moledo-venv/poppler/Library/bin')
    images[0].save(file,'JPEG')
"""

p = pathlib.Path('test/test2')

for image in p.iterdir():
    images = convert_from_path(image,poppler_path='moledo-venv/poppler/Library/bin')
    images[0].save(image, 'JPEG') # image saves to correct path