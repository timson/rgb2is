# Intro
Utility for finding closest color for given rgb values from colors database.  By default it using Nirlat (IS) colors database.

Nirlat is Israel-based company producing paints and coating.

To find closest color I using CIEDE2000 formula from colormath library.

## How to install
  pip install -r requirements.txt

## How to run
  rgb2is.py -r 115 -g 143 -b 142

This command will print nbest (by default it is 3) closest color from  colors.json database. By default this database maden from Nirlat (IS) colors.
