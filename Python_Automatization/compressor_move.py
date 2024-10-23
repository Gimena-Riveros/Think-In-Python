from PIL import Image # python3 -m pip install Pillow

import os

downloadsFolder = "/Users/gimen/Documents/"     #   from
picturesFolder = "/Users/gimen/Documents/"      #   to

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)