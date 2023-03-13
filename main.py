#!/usr/bin/env
import argparse
import math
import os
import sys
import time


parser = argparse.ArgumentParser(
    description="Placeholder description."
)
parser.add_argument("whole_number", help="Whole number to iterate.", type=int)
parser.add_argument(
    "-e", "--exponent", default=2, help="Exponent placeholder", type=int
)
parser.add_argument(
    "-l", "--limit", default=5, help="Set the limit.", type=int
)
parser.add_argument(
    "-c", "--clean", help="Clear the console on execution.", action='store_true'
)
args = parser.parse_args()

if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.whole_number:
    print("Whole number required!")
    parser.print_help()
    sys.exit(1)


def power_tree(num_in):

    tree = []
    exp = args.exponent
    limit = args.limit
    x = int(num_in)
    for i in range(0,limit):
        # time.sleep(1)
        num_squared = square(x, exp)
        tree.append(round(num_squared))
        x = num_squared

    #print(f"Length of returned array: {len(tree)}")
    #print(f"Length of last item: {len(str(tree[len(tree) - 1]))}")

    display_output(tree)


def display_output(tree):

    max_len = len(str(tree[len(tree) - 1]))
    num_list = tree

    print("\n")
    for i in tree:
        x = f"{i:-<{max_len}}"
        #print(f"{i:-<{max_len}}")
        for y in x:
            time.sleep(0.1)
            print(y, end="")
        print("\n")
        i+=1


def square(num_in, exp):
    num_out = math.pow(num_in, exp)
    return num_out


def main():

    if args.clean:
        os.system("cls")
    
    i = args.whole_number
    try:
        power_tree(i)
    except KeyboardInterrupt:
        print("\n\nUser exited program.")
        sys.exit(1)        
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
