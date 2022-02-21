import unittest

from predictive_values import diagnoses, count_positives, count_negatives, count_accurate, count_inaccurate, count_tests, calc_pos_pred_value, calc_neg_pred_value, positive_predictive_value, negative_predictive_value

class Test_positive_or_negative_counts(unittest.TestCase):

    def test_count_positive(self):
        self.assertAlmostEqual(23, count_positives(diagnoses))

    def test_count_negatives(self):
        self.assertAlmostEqual(27, count_negatives(diagnoses))

    def test_counts(self):
        self.assertAlmostEqual(50, count_tests(diagnoses))

class Test_accurate_or_inaccurate(unittest.TestCase):

    def test_count_accurate_True(self):
        self.assertAlmostEqual(10, count_accurate(True, diagnoses))

    def test_count_accurate_False(self):
        self.assertAlmostEqual(15, count_accurate(False, diagnoses))

    def test_count_inaccurate_True(self):
        self.assertAlmostEqual(13, count_inaccurate(True, diagnoses))

    def test_count_inaccurate_False(self):
        self.assertAlmostEqual(12, count_inaccurate(False, diagnoses))

class Test_posAndneg_PredValue(unittest.TestCase):

    def test_PosPredValue(self):
        self.assertAlmostEqual(100.0, positive_predictive_value)

    def test_NegPredValue(self):
        self.assertAlmostEqual(100.0, negative_predictive_value)


class TestRandomPosAndNegPredValue(unittest.TestCase):

    RandomDI = [(True, False), (True, True), (True, False), (True, False),
                 (False, True), (True, True), (False, True), (False, False),
                 (True, True), (False, True), (False, False), (True, False),
                 (False, False), (True, True), (True, False), (True, True),
                 (True, False), (False, True), (False, True), (False, True),
                 (True, True), (True, True), (False, True), (False, True),
                 (False, True), (True, True), (False, False), (False, False),
                 (False, True), (False, False), (False, True), (True, False),
                 (True, False), (True, False), (True, True), (False, True),
                 (True, False), (True, False), (True, False), (False, False),
                 (False, True), (False, True), (True, True), (True, False),
                 (True, False), (True, True), (False, False), (False, True),
                 (True, True), (False, False), (False, False), (True, False),
                 (True, False), (True, False), (False, True), (True, True),
                 (False, True), (True, False), (True, True), (False, False),
                 (True, True), (False, True), (False, False), (True, False),
                 (False, False), (True, True), (True, False), (True, True),
                 (True, True), (False, True), (False, True), (False, True),
                 (True, True), (True, True), (False, True), (False, True),
                 (False, True), (True, True), (False, False), (False, False),
                 (False, True), (False, False), (False, True), (True, True),
                 (True, True), (True, False), (True, True), (False, False),
                 (True, True), (True, False), (False, False), (False, False),
                 (False, True), (True, False), (True, True), (False, False),
                 (True, False), (True, True), (False, False), (True, False)]

    def testCountRandomDI(self):
        self.assertAlmostEqual(100, count_tests(self.RandomDI))

    def test_PosPredValueRandom(self):
        self.assertAlmostEqual(100.0, calc_pos_pred_value(count_accurate(True, self.RandomDI), count_inaccurate(True, self.RandomDI), count_positives(self.RandomDI), count_tests(self.RandomDI)))

    def test_NegPredValueRandom(self):
        self.assertAlmostEqual(100.0, calc_pos_pred_value(count_accurate(False, self.RandomDI), count_inaccurate(False, self.RandomDI),count_negatives(self.RandomDI), count_tests(self.RandomDI)))


if __name__ == '__main__':
    unittest.main()
