#!/usr/bin/env python3

##############################
# TheWallpaperProject Driver #
##############################

from thewallpaperproject import combine_images
import argparse
from math import log

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', "-i", help='Path to input directory: string')
    parser.add_argument('--output', "-o", help='Path to output file: string')
    parser.add_argument('--background', "-b", help='Background color: "#eeeeee"')
    parser.add_argument('--backgroundpath', "-bp", help='Background image path: string')
    parser.add_argument('--strictness', "-s", help='Strictness: int')
    parser.add_argument('--factor', "-f", help='Factor: int')
    parser.add_argument('--width', "-w", help='Target width: int')
    parser.add_argument('--height', "-he", help='Target height: int')
    parser.add_argument('--count', "-c", help='Count of files to merge: int')
    parser.add_argument('--margin', "-m", help='Min distance  between the edge and pictures: int')
    parser.add_argument('--padding', "-p", help='Min distance between any side of a pic to another pic: int')
    args = parser.parse_args()

    input_path = None
    if args.input:
        input_path = args.input

    if not input_path:
        raise Exception("Input directory is undefined. Make sure to define it with the --input or -i flag.")

    output_path = None
    if args.output:
        output_path = args.output

    background = "#eeeeee"
    if args.background:
        background = args.background

    bg_path = None
    if args.backgroundpath:
        bg_path = args.backgroundpath

    count = 2
    if args.count:
        count = int(args.count)
    if count <= 0:
        raise Exception("Make sure the count flag is positive.")

    strictness = 50
    if args.strictness:
        strictness = int(args.strictness)
    if strictness <= 0:
        raise Exception("Make sure the strictness flag is positive")
    permutations = int((count * count) / log(count)) if count >= 2 else 5
    # permutations = 5

    factor = 3
    if args.factor:
        factor = int(args.factor)
    if factor <= 0:
        raise Exception("Make sure the scaling factor is larger than 1")

    res = None
    if args.width and args.height:
        res = (int(args.width), int(args.height))

    if not res:
        raise Exception("Target resolution cannot be undefined. Make sure to use the width and height params.")

    margin = 0
    if args.margin:
        margin = int(args.margin)
    if margin < 0:
        raise Exception("Make sure the margin flag is not negative.")

    padding = 0
    if args.padding:
        padding = int(args.padding)
    if padding < 0:
        raise Exception("Make sure the padding flag is not negative.")

    print("Calculating sizes and coordinates...")
    if not output_path:
        combine_images(input_path=input_path, bg_color=background, strictness=strictness, fact_main=factor, target_size=res,
                       count=count, margin=margin, padding=padding, permutations=permutations, background_path=bg_path)
    else:
        combine_images(input_path=input_path, output_path=output_path, bg_color=background, strictness=strictness, fact_main=factor,
                       target_size=res, count=count, margin=margin, padding=padding, permutations=permutations,
                       background_path=bg_path)
    print("Done")
