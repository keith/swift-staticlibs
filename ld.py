#!/usr/bin/env python

import argparse
import subprocess


def ld_command(arch, isysroot, filelist, output):
    return [
        "libtool",
        "-static",
        "-arch_only", arch,
        "-syslibroot", isysroot,
        "-filelist", filelist,
        "-o", output,
    ]


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-arch", required=True)
    parser.add_argument("-isysroot", required=True)
    parser.add_argument("-filelist", required=True)
    parser.add_argument("-o", dest="output", required=True)
    return parser

if __name__ == "__main__":
    arguments, _ = build_parser().parse_known_args()
    command = ld_command(arguments.arch, arguments.isysroot,
                         arguments.filelist, arguments.output)
    print(" ".join(command))
    print(subprocess.check_output(command))
