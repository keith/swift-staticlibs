import lipo
import unittest


class TestLipo(unittest.TestCase):
    def test_valid_command(self):
        inputs = ["/foo/x86_64/Executable"]
        output = "/foo/Executable"
        command = " ".join(lipo.lipo_command(inputs, output))
        expected_command = " ".join([
            "lipo",
            "-create", "/foo/x86_64/Executable",
            "-output", "/foo/Executable"
        ])
        self.assertEqual(command, expected_command)

    def test_valid_command_multiple_inputs(self):
        inputs = ["/foo/x86_64/Executable", "/foo/i386/Executable"]
        output = "/foo/Executable"
        command = " ".join(lipo.lipo_command(inputs, output))
        expected_command = " ".join([
            "lipo",
            "-create",
            "/foo/x86_64/Executable",
            "/foo/i386/Executable",
            "-output",
            "/foo/Executable"
        ])
        self.assertEqual(command, expected_command)

    def test_argument_parser(self):
        parser = lipo.build_parser()
        arguments = parser.parse_args([
            "-create", "/foo/i386/executable", "/foo/x86_64/executable",
            "-output", "/foo/output",
        ])

        self.assertEqual(arguments.inputs,
                         ["/foo/i386/executable", "/foo/x86_64/executable"])
        self.assertEqual(arguments.output, "/foo/output")
