#!/bin/sh

for I in 1 2 3 4 5 6 7 8 9 10 11
do
    python3 image_filter.py -i images/$1.png -m h$I -o $2/$1_h$I.png -oc $2/$1_h${I}_comb.png
done