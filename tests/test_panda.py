import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from panda import guaranteed_harvest


class HarvestTests(unittest.TestCase):
    def test_precision_schedule(self):
        self.assertEqual(guaranteed_harvest([2001, 1999, 1000], [0, 1, 0, 2], 100), 4000)

    def test_single_plot(self):
        self.assertEqual(guaranteed_harvest([10], [0], 10), 10)

    def test_schedule_is_not_mutated(self):
        schedule = [0, 1]
        guaranteed_harvest([10, 5], schedule, 10)
        self.assertEqual(schedule, [0, 1])


if __name__ == "__main__":
    unittest.main()
