import unittest
from earliest_full_bloom import Solution


class TestEarliestFullBloom(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_minimum_input_size(self):
        plantTime = [1]
        growTime = [1]
        self.assertEqual(self.solution.earliestFullBloom(plantTime, growTime), 2)

    def test_maximum_input_size(self):
        plantTime = [1] * 105
        growTime = [1] * 105
        self.assertEqual(self.solution.earliestFullBloom(plantTime, growTime), 106)

    def test_varying_plant_and_grow_times(self):
        plantTime = [1, 2, 3]
        growTime = [3, 2, 1]
        self.assertEqual(self.solution.earliestFullBloom(plantTime, growTime), 7)

    def test_identical_plant_and_grow_times(self):
        plantTime = [2, 2, 2]
        growTime = [2, 2, 2]
        self.assertEqual(self.solution.earliestFullBloom(plantTime, growTime), 8)

    def test_large_values(self):
        plantTime = [104] * 105
        growTime = [104] * 105
        self.assertEqual(self.solution.earliestFullBloom(plantTime, growTime), 11024)

    def test_edge_values(self):
        plantTime = [1, 2, 1, 1, 1]
        growTime = [2, 9, 9, 1, 1]
        self.assertEqual(self.solution.earliestFullBloom(plantTime, growTime), 12)


if __name__ == "__main__":
    unittest.main()
