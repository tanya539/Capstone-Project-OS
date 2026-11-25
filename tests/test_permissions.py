import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

BITS = {"r": 4, "w": 2, "x": 1}

def permission_value(read=False, write=False, execute=False):
    return (4 if read else 0) + (2 if write else 0) + (1 if execute else 0)

def symbolic(read=False, write=False, execute=False):
    return ("r" if read else "-") + ("w" if write else "-") + ("x" if execute else "-")

class PermissionLogicTests(unittest.TestCase):
    def test_assignment_example(self):
        self.assertEqual(symbolic(True, True, False), "rw-")
        self.assertEqual(symbolic(True, False, False), "r--")
        self.assertEqual(symbolic(False, False, False), "---")
        self.assertEqual("".join(map(str, [
            permission_value(True, True, False),
            permission_value(True, False, False),
            permission_value(False, False, False)
        ])), "640")

    def test_all_permissions(self):
        self.assertEqual(permission_value(True, True, True), 7)
        self.assertEqual(symbolic(True, True, True), "rwx")

    def test_no_permissions(self):
        self.assertEqual(permission_value(), 0)
        self.assertEqual(symbolic(), "---")

if __name__ == "__main__":
    unittest.main()
