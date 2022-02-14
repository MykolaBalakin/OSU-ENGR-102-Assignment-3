import unittest

from z_score import z_score, mean, stdev, greatest, least, population

class TestUtils(unittest.TestCase):

    def test_mean(self):
        self.assertAlmostEqual(51.94, mean(population))

    def test_stdev(self):
        self.assertAlmostEqual(27.97027708, stdev(population, mean(population)))

class TestZScorePopulation(unittest.TestCase):

    def test_mean_population(self):
        self.assertAlmostEqual(0, z_score(mean(population), population))

    def test_greatest_population(self):
        self.assertAlmostEqual(1.646748077, z_score(greatest(population), population))

    def test_least_population(self):
        self.assertAlmostEqual(-1.821218998, z_score(least(population), population))

class TestZScoreRandom(unittest.TestCase):

    data_set = [ -34, 24, 39, -20, 19, -34, -18, -5, 25, 28 ]

    def test_0(self):
        self.assertAlmostEqual(-0.091563046, z_score(0, self.data_set))

    def test_p10(self):
        self.assertAlmostEqual(0.289949645, z_score(10, self.data_set))

    def test_p20(self):
        self.assertAlmostEqual(0.671462335, z_score(20, self.data_set))

    def test_n10(self):
        self.assertAlmostEqual(-0.473075736, z_score(-10, self.data_set))

    def test_n20(self):
        self.assertAlmostEqual(-0.854588426, z_score(-20, self.data_set))

if __name__ == '__main__':
    unittest.main()