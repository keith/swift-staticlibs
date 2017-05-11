import ld
import unittest


class TestLd(unittest.TestCase):
    def test_valid_command(self):
        arch = "x86_64"
        syslibroot = "/foo/bar/baz"
        library_search_path = "/foo/bar/lib"
        filelist = "/foo/filelist.txt"
        linked_libraries = ["First", "Second"]
        output = "/foo/Executable"

        command = " ".join(ld.ld_command(arch, syslibroot, library_search_path,
                                         linked_libraries, filelist, output))
        expected_command = " ".join([
            "libtool",
            "-static",
            "-arch_only", "x86_64",
            "-syslibroot", "/foo/bar/baz",
            "-L/foo/bar/lib",
            "-filelist", "/foo/filelist.txt",
            "-lFirst", "-lSecond",
            "-o", "/foo/Executable",
        ])
        self.assertEqual(command, expected_command)

    def test_no_linked_libraries(self):
        arch = "x86_64"
        syslibroot = "/foo/bar/baz"
        library_search_path = "/foo/bar/lib"
        filelist = "/foo/filelist.txt"
        linked_libraries = []
        output = "/foo/Executable"

        command = " ".join(ld.ld_command(arch, syslibroot, library_search_path,
                                         linked_libraries, filelist, output))
        expected_command = " ".join([
            "libtool",
            "-static",
            "-arch_only", "x86_64",
            "-syslibroot", "/foo/bar/baz",
            "-L/foo/bar/lib",
            "-filelist", "/foo/filelist.txt",
            "-o", "/foo/Executable",
        ])
        self.assertEqual(command, expected_command)

    def test_argument_parser(self):
        parser = ld.build_parser()
        arguments = parser.parse_args([
            "-arch", "x86_64",
            "-isysroot", "/foo/bar",
            "-filelist", "/foo/files.txt",
            "-o", "/foo/output",
            "-L/foo", "-L/bar",
            "-lFirst", "-lSecond",
        ])

        self.assertEqual(arguments.arch, "x86_64")
        self.assertEqual(arguments.isysroot, "/foo/bar")
        self.assertEqual(arguments.filelist, "/foo/files.txt")
        self.assertEqual(arguments.output, "/foo/output")
        self.assertEqual(arguments.library_paths, ["/foo", "/bar"])
        self.assertEqual(arguments.linked_libraries, ["First", "Second"])

    def test_argument_parser_without_linked_libraries(self):
        parser = ld.build_parser()
        arguments = parser.parse_args([
            "-arch", "x86_64",
            "-isysroot", "/foo/bar",
            "-filelist", "/foo/files.txt",
            "-o", "/foo/output",
            "-L/foo", "-L/bar",
        ])

        self.assertEqual(arguments.arch, "x86_64")
        self.assertEqual(arguments.isysroot, "/foo/bar")
        self.assertEqual(arguments.filelist, "/foo/files.txt")
        self.assertEqual(arguments.output, "/foo/output")
        self.assertEqual(arguments.library_paths, ["/foo", "/bar"])
        self.assertEqual(arguments.linked_libraries, [])
