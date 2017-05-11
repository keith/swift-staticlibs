import paths
import unittest


class TestPaths(unittest.TestCase):
    def test_developer_bin_directory(self):
        toolchain = "/foo/bar"
        expected_path = "/foo/bar/usr/bin"
        self.assertEqual(paths.bin_directory(toolchain), expected_path)

    def test_developer_bin_directory_trailing_slash(self):
        toolchain = "/foo/XcodeDefault.xctoolchain/"
        expected_path = "/foo/XcodeDefault.xctoolchain/usr/bin"
        self.assertEqual(paths.bin_directory(toolchain), expected_path)

    def test_executable_path(self):
        toolchain = "/foo/XcodeDefault.xctoolchain/"
        expected_path = "/foo/XcodeDefault.xctoolchain/usr/bin/lipo"
        self.assertEqual(paths.executable_path(toolchain, "lipo"),
                         expected_path)

    def test_get_toolchain_dir(self):
        env = {"TOOLCHAIN_DIR": "/foo/bar"}
        self.assertEqual(paths.get_toolchain_dir(env), "/foo/bar")
