#!/usr/bin/python3
"""
Test for the console.py
"""

import cmd
import json
import os
import unittest
from io import StringIO
from itertools import count
from unittest.mock import patch

import pycodestyle

import console
import models
from console import HBNBCommand
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestBasicCaseAndDoc(unittest.TestCase):
    """
    Test the whole docs, and basic input
    """

    def test_doc(self):
        """
        Check all the doc of the Amenity Class
        """
        # module documentation
        module = len(console.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(HBNBCommand.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_all.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_create.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_destroy.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_quit.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_EOF.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_destroy.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_update.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.emptyline.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.default.__doc__)
        self.assertGreater(module_class, 0)

    def test_pycodeStyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def test_emptyline(self):
        """
        Check the case of empty line
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_UnknowCommand(self):
        """
        Test an unknow command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("fdfdf")
            self.assertEqual("*** Unknown syntax: fdfdf", f.getvalue().strip())
