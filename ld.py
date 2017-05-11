#!/usr/bin/env python

import argparse
import subprocess


def ld_command(arch, isysroot, library_search_path, linked_libraries, filelist,
               output):
    return [
        "libtool",
        "-static",
        "-arch_only", arch,
        "-syslibroot", isysroot,
        "-L{}".format(library_search_path),
        "-filelist", filelist,
    ] + ["-l{}".format(x) for x in linked_libraries] + [
        "-o", output,
    ]


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-arch", required=True)
    parser.add_argument("-isysroot", required=True)
    parser.add_argument("-filelist", required=True)
    parser.add_argument("-o", dest="output", required=True)
    parser.add_argument("-L", action="append", dest="library_paths",
                        required=True)
    parser.add_argument("-l", action="append", dest="linked_libraries",
                        default=[])
    return parser

if __name__ == "__main__":
    arguments, _ = build_parser().parse_known_args()
    command = ld_command(arguments.arch, arguments.isysroot,
                         arguments.library_paths[0],
                         arguments.linked_libraries, arguments.filelist,
                         arguments.output)
    print(" ".join(command))
    print(subprocess.check_output(command))
