import os
import json
from PIL import Image

COLOR_PATH = 'colors'


def gen_colorsdb():
    colors = {}
    for fn in [x for x in os.listdir(COLOR_PATH) if x.endswith('.jpg')]:
        full_fn = os.path.join(COLOR_PATH, fn)
        im = Image.open(full_fn)
        rgb = im.getpixel((0,0))
        name, _ = fn.split('.')
        colors[name] = rgb

    with open('colors.json', 'w') as fout:
        fout.write(json.dumps(colors, indent=4))

if __name__ == '__main__':
    gen_colorsdb()
