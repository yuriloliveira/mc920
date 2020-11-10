#!/bin/sh

mkdir -p $2
for E in 'a' 'b' 'c' 'd' 'e' 'f'
do
    echo "Processing image images/$1.png with error distribution '$E'..."
    python3 halftoning.py -i images/$1.png -ed $E -o $2/$1_$E.png -ss
    echo "Processing image images/$1.png with error distribution '$E' and sweep mode alternate..."
    python3 halftoning.py -i images/$1.png -ed $E -o $2/$1_${E}_alternate.png -ss -sm alternate
done