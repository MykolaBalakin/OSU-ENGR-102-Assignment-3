import unittest

from predictive_values_2 import calc_pos_pred_value, calc_neg_pred_value, count_accurate, count_inaccurate, count_positives, count_tests

class Tests(unittest.TestCase):

    data_set_1 = [(True, True), (True, False), (False, True), (False, True), (False, False)]
    data_set_2 = [(True, True), (True, False), (True, False), (False, True), (False, True), (False, True), (False, False)]

    def test_pos_pred_value(self):
        self.assertAlmostEqual(1, count_accurate(True, self.data_set_1))

    def test_pos_pred_value(self):
        self.assertAlmostEqual(1, count_inaccurate(True, self.data_set_1))

    def test_pos_pred_value(self):
        self.assertAlmostEqual(2, count_positives(self.data_set_1))

    def test_pos_pred_value(self):
        self.assertAlmostEqual(5, count_tests(self.data_set_1))

    def test_positive_data_set_1(self):
        self.assertAlmostEqual(50, calc_pos_pred_value(self.data_set_1))

    def test_positive_data_set_2(self):
        self.assertAlmostEqual(33.3333333, calc_pos_pred_value(self.data_set_2))

    def test_negative_data_set_1(self):
        self.assertAlmostEqual(66.6666667, calc_neg_pred_value(self.data_set_1))

    def test_negative_data_set_2(self):
        self.assertAlmostEqual(75, calc_neg_pred_value(self.data_set_2))

if __name__ == '__main__':
    unittest.main()
