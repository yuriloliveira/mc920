#!/bin/sh

mkdir -p $2
for M in 'global' 'bernsen' 'niblack' 'sauvola' 'phansalskar' 'contrast' 'mean' 'median'
do
    echo "Applying method $M in image 'images/$1.pgm'..."
    python3 thresholding.py -i images/$1.pgm -m $M -o $2/$1_$M.pgm -dm off
done