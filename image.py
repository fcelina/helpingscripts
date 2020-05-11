import os, sys
from PIL import Image

def convert(path, path2, format):
    for (root,dirs,files) in os.walk(path):
        for file in files:
            f, e = os.path.splitext(file)
            new = os.path.join(path2,f)
            convert = f + format
            if file != f:
                try:
                    with Image.open(file) as im:
                        im.save(new, format)
                except IOError:
                    pass

path = input("Enter your directory here: ")
path2 = input("Enter the directory you want to export to: ")
format = input("Enter the format you wish to convert to: ")
if __name__ == "__main__":
    convert(path, path2, format)
