import json
import click
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

@click.command()
@click.option('--nbest', default=3, help='Amount of best result to print.')
@click.option('--colorsdb', default='colors.json', help='Colors datafile to use.')
@click.option('-g', '--green', required=True, type=click.IntRange(0, 255), help='Red value')
@click.option('-r', '--red', required=True, type=click.IntRange(0, 255), help='Green value')
@click.option('-b', '--blue', required=True, type=click.IntRange(0, 255), help='Blue value')
def rgb2is(red, green, blue, colorsdb, nbest):
    colors = json.loads(open(colorsdb, 'r').read())
    color1_rgb = sRGBColor(red, green, blue, is_upscaled=True);
    color1_lab = convert_color(color1_rgb, LabColor);
    result = []

    for name, value in colors.items():
        color2_rgb = sRGBColor(*value, is_upscaled=True);
        color2_lab = convert_color(color2_rgb, LabColor);
        delta_e = delta_e_cie2000(color1_lab, color2_lab);
        result.append((delta_e, name))

    for res in sorted(result)[:nbest]:
        print('{1}, delta = {0}'.format(*res))


if __name__ == '__main__':
    rgb2is()
