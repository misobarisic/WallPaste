##############################
# TheWallpaperProject Module #
##############################

import os
import random
from math import sqrt
from PIL import Image, ImageOps


def combine_images(input_path=None, images=None, output_path=None, target_size=None,
                   strictness=50, count=2, fact_main=2,
                   margin=0, padding=0, permutations=5,
                   bg_color="#eeeeee", background=None, background_path=None):
    """
    This function will calculate the corresponding image sizes and their coordinates and paste them on
    the background image without them intersecting.
    :param input_path: input directory where source images are located
    :param count: number of images to use (used with input_path)
    :param images: list of full paths of images (does not have to be in the same directory)
    :param output_path: output path where the generated image will be saved
    :param target_size: tuple representing the target (width, height)
    :param background: PIL Image object which will be used as the background
    :param background_path: Path to the image that will be used as the background (use only if background is not specified)
    :param bg_color: if background PIL image is not specified, use this to specify the background color
    :param target_size: target image resolution
    :param permutations: number of image order shuffles before changing the scaling factor by one
    :param strictness: number of tries before making a permutation
    :param fact_main: starting scaling factor
    :param margin: minimal distance between the edges and placed images (in px)
    :param padding: minimal distance between each image (in px)
    :return:
    """

    if not input_path:
        raise Exception("input_path must be defined")
    if not target_size:
        raise Exception("target_size must be defined")

    # Initial setup
    if images is None:
        images = list()
    image_sizes = dict()
    reachedStrictness = False
    strictness0 = strictness - 1
    width, height = target_size
    fact = sqrt(fact_main)

    if not images:
        files = os.listdir(input_path)
        paths = random.sample(files, count)
        images = list(map(lambda path: f'{input_path}/{path}', paths))

    while True:
        for i in range(permutations):
            # Used coords set
            coords = set()
            # List of tuples representing the (x, y) value of each images
            image_coords = list()
            # Resized image sizes
            final_sizes = list()
            for image in images:
                reachedStrictness = False
                try:
                    size = image_sizes[image]
                    im_w, im_h = size
                except KeyError:
                    im = Image.open(image)
                    im_w, im_h = im.size
                    image_sizes.update({image: im.size})

                ratio = im_w / im_h
                if im_w > width:
                    im_w = width
                    im_h = im_w / ratio
                if im_h > height:
                    ratio = im_w / im_h
                    im_h = height
                    im_w = im_h * ratio

                im_w = int(im_w / fact)
                im_h = int(im_h / fact)

                x = random.randint(margin, width - im_w - margin)
                y = random.randint(margin, height - im_h - margin)

                for j in range(strictness):
                    if j == strictness0:
                        random.shuffle(images)
                        reachedStrictness = True
                        break
                    image_set = set()
                    # Horizontal border coords
                    for x_r in range(x, x + im_w + 1):
                        image_set.add((x_r, y))
                        image_set.add((x_r, y + im_h))
                    # Vertical border coords
                    for y_r in range(y + 1, y + im_h):
                        image_set.add((x, y_r))
                        image_set.add((x + im_w, y_r))

                    # Check for set intersection
                    state = image_set & coords
                    if state:
                        x = random.randint(margin, width - im_w - margin)
                        y = random.randint(margin, height - im_h - margin)
                    else:
                        break

                if reachedStrictness:
                    fact_main += 1
                    fact = sqrt(fact_main)
                    break

                # Set of tuples representing used (x,y) coordinates
                for x_r in range(x - padding, x + im_w + 1 + padding):
                    for y_r in range(y - padding, y + im_h + 1 + padding):
                        coords.add((x_r, y_r))

                # Store calculated values
                image_coords.append((x, y))
                final_sizes.append((im_w, im_h))

            if reachedStrictness:
                reachedStrictness = False
            else:
                return generate_image(images, final_sizes, image_coords, output_path=output_path, background=background,
                                      target_size=target_size, bg_color=bg_color, background_path=background_path)


def generate_image(images, sizes, image_coords, output_path=None,
                   background=None, background_path=None,
                   bg_color="#eeeeee", target_size=(1920, 1080)):
    """
    Paste images onto the background and output it to the output_path if defined,
    if not, open the generated image in an image viewer.
    :param images: list of full image paths
    :param sizes: list of (width, height) tuples relating to every image
    :param image_coords: list of (x,y) tuples representing the top left coordinates of every image
    :param background: PIL Image which will be used as the background
    :param background_path: Path to the image that will be used as the background (use only if background is not specified)
    :param bg_color: if background PIL image is not specified, use this to specify the background color (used only with target_size)
    :param target_size: target image resolution (used only with bg_color)
    :param output_path: The generated image will be saved here
    """

    if not background and background_path:
        background = ImageOps.fit(Image.open(background_path), target_size)
    elif not background and not background_path and bg_color and target_size:
        background = Image.new("RGB", target_size, bg_color)

    if background.size != target_size:
        background = ImageOps.fit(background, target_size)

    images = images[0:len(images)]
    for ind, image in enumerate(images):
        background.paste(ImageOps.fit(Image.open(image), sizes[ind]), image_coords[ind])
    if output_path:
        background.save(output_path)
    else:
        background.show()


if __name__ == '__main__':
    print("thewallpaperproject.py should not be run as a normal script. Its functions are intended to be imported.")
