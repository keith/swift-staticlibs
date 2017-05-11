#!/usr/bin/env python

import argparse
import paths
import subprocess


def lipo_command(inputs, output):
    return [
        "lipo",
        "-create"
    ] + inputs + [
        "-output", output,
    ]


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-create", dest="inputs", nargs="+", required=True)
    parser.add_argument("-output", required=True)
    return parser

if __name__ == "__main__":
    arguments = build_parser().parse_args()
    command = lipo_command(arguments.inputs, arguments.output)
    print(" ".join(command))
    print(subprocess.check_output(command))
