import os


def get_toolchain_dir(env=os.environ):
    return env["TOOLCHAIN_DIR"]


def bin_directory(toolchain):
    return os.path.join(toolchain, "usr/bin")


def executable_path(toolchain, executable):
    return os.path.join(bin_directory(toolchain), executable)
