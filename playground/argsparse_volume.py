import math
import argparse

parser = argparse.ArgumentParser(description="Calculate Volume of a Cylinder")
parser.add_argument('-r', '--radius', type=int, metavar='', required=True, help='Radius of the Cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of the Cylinder')
groups = parser.add_mutually_exclusive_group()
groups.add_argument('-q', '--quiet', action='store_true', help='Quiet Mode')
groups.add_argument('-v', '--verbose', action='store_true', help='Verbose Mode')
args = parser.parse_args()


def volume_of_cylinder(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume


if __name__ == '__main__':
    volume = volume_of_cylinder(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print(f"Volume of Cylinder with radius = {args.radius} and height {args.height} is {volume}")
    else:
        print("Volume of Cylinder is = %s" % volume)
