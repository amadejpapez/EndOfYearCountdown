import os

import requests
from auth_secrets import keys
from PIL import Image
from pyunsplash import PyUnsplash

DIRPATH = os.path.dirname(os.path.realpath(__file__))


def get_image(season):
    # request image from Unsplash
    unsplash = PyUnsplash(api_key=keys["PyUnsplash"]["api_key"])
    image = unsplash.photos(
        type_="random",
        count=1,
        featured=True,
        orientation="landscape",
        query=season,
    )

    optimize_image(image, season)


def optimize_image(image, season):
    for image in image.entries:
        # download image to the current folder
        img_data = requests.get(image.link_download).content

        with open(f"{DIRPATH}/photo.jpg", "wb") as myFile:
            myFile.write(img_data)

        if os.path.getsize(f"{DIRPATH}/photo.jpg") >= 3200000:
            # if image is bigger than 3.2 MB, take another one
            get_image(season)

        while os.path.getsize(f"{DIRPATH}/photo.jpg") >= 3072000:
            # if image is larger than 3.072 MB, optimize it as larger size will cause an error
            image = Image.open(f"{DIRPATH}/photo.jpg")
            image.resize((1080, 566), Image.ANTIALIAS)
            image.save(f"{DIRPATH}/photo.jpg", quality=80)
