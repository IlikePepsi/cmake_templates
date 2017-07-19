#!/usr/bin/env python

import argparse
import fileinput

parser = argparse.ArgumentParser()
parser.add_argument("input_list", help="cmake list of input files")
parser.add_argument("output_list", help="cmake list of outpur files")

args = parser.parse_args()

def main():

    input_files = str(args.input_list).split(';')
    output_files = str(args.output_list).split(';')

    assert len(input_files) == len(output_files), \
            "list length differ: %r != %r" % (len(input_files), len(output_files))

    zipped = zip(input_files, output_files)

    for e in zipped:
        out_file = open(e[1], 'w+')

        with fileinput.input(e[0]) as in_file:
            for line in in_file:
                out_file.write(line.replace('@', ' '))

        out_file.close()

if __name__ == '__main__':
    main()
