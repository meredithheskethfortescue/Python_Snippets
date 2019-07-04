#!/usr/bin/env python3
"""Minimal example for test driven development using the unittest framework"""

import unittest


def hello_world() -> str:
    return "Hello, world!"


class TestHelloWorld(unittest.TestCase):
    def test_returns_helloworld(self):
        self.assertEqual(hello_world(), "Hello, world!")

    def tearDown(self) -> None:
        print("teardown")


if __name__ == '__main__':
    unittest.main()
