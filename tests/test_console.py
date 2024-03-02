#!/usr/bin/python3
"""Test for console.py"""
import os
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsoleClass(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""

        FileStorage.__objects = {}
        self.HBNB = HBNBCommand()

    def test_emptyline(self):
        """Test for empty line"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test for quit command"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("quit")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """Test for EOF command"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.HBNB.onecmd("EOF"))

    def test_create_errors(self):
        """Test for create command errors"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Maga")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_show(self):
        """Test for show command errors"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show Maga")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("show BaseModel abcd-123")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test for destroy command errors"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy Maga")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def tearDown(self):
        """Clean the test"""

        try:
            os.remove("file.json")
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
