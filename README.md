# WallPaste

A tool that allows you to paste multiple images onto a background with respect of their aspect ratio.

This project is both a Python library/module and a CLI utility.

### Requirements

- [pillow](https://github.com/python-pillow/Pillow)

### Installation

- pip: `pip3 install wallpaste`
- cloning the repo and running `pip3 install -r requirements.txt`

### CLI

Example usage:

```bash
# If installed by PIP
python3 -m wp -i ~/Images -o ~/out.jpg -c 8
# or
python3 -m wp --input ~/Images --output ~/out.jpg --count 8

# If installed manually (git clone)
python3 /path/to/wp.py --input="~/Images" --output="~/out.jpg" --count=8
```

#### Flags

| Flag |  Shorthand  | Description | Required |
|:---|:---:|:---:|---:|
| --input  | -i | Path to input directory| yes |
| --output  | -o | Path to output file | no |
| --background  | -b | Background color  | yes* |
| --backgroundpath  | -bp | Path to background image | yes* |
| --strictness  | -s | Strictness number | no |
| --factor  | -f | Starting scale factor | no |
| --width  | -w | Target width (in px) | yes |
| --height  | -he | Target height (in px) | yes |
| --count  | -c | Number of images to merge | no |
| --margin  | -m | Min distance between the edge and images | no |
| --padding  | -p | Min distance between any side of a pic to another pic | no |

* _backgroundpath_ only needs to be specified when _background_ is not

### Module usage

If you've installed this package using pip, you can import it like this:

```python
import wallpaste
# or
from wallpaste import combine_images, generate_image
```

There are numerous function parameters to each function. No point in listing it all here, but their docs are located
next to their definition in `thewallpaperproject.py`.

```python
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
```

```python
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
```

### Author

👤 **Mišo Barišić**

* Website: https://www.misobarisic.com
* GitHub: [@misobarisic](https://github.com/misobarisic)
* GitLab: [@misobarisic](https://gitlab.com/misobarisic)

### Show your support

Give a ⭐️ if this project helped you!

### 📝 License

This project is [MIT](https://github.com/misobarisic/SafePaste/blob/master/LICENSE) licensed.
