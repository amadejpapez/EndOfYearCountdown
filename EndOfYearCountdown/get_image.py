import os

import wget
from auth_secrets import keys
from PIL import Image
from pyunsplash import PyUnsplash

dirPath = os.path.dirname(os.path.realpath(__file__))


def get_image(season):
    # get image from Unsplash
    unsplash = PyUnsplash(api_key=keys["PyUnsplash"]["api_key"])
    image = unsplash.photos(
        type_="random",
        count=1,
        featured=True,
        orientation="landscape",
        query=season,
    )

    if os.path.exists(f"{dirPath}/photo.jpg"):
        # remove previous "photo"
        os.remove(f"{dirPath}/photo.jpg")

    optimize_image(image, season)


def optimize_image(image, season):
    for image in image.entries:
        # download image to the current folder
        wget.download(image.link_download, out=f"{dirPath}/photo.jpg")

        if os.path.getsize(f"{dirPath}/photo.jpg") >= 3200000:
            # if image is bigger than 3.2 MB, take another one
            get_image(season)

        while os.path.getsize(f"{dirPath}/photo.jpg") >= 3072000:
            # if image is larger than 3.072 MB, optimize it as larger size will cause an error
            image = Image.open(f"{dirPath}/photo.jpg")
            image.resize((1080, 566), Image.ANTIALIAS)
            image.save(f"{dirPath}/photo.jpg", quality=80)
