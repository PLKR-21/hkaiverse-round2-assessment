import unittest

def net_minutes(requests, current, proposed, review, support):
    return requests * (current - proposed) - review - support

def affected_share(affected, total):
    if total <= 0:
        raise ValueError("total must be positive")
    if affected < 0 or affected > total:
        raise ValueError("affected must be between zero and total")
    return 100 * affected / total

class ProjectLogicTests(unittest.TestCase):
    def test_base_scenario(self):
        self.assertEqual(net_minutes(40, 12, 7, 60, 30), 110)

    def test_low_scenario(self):
        self.assertEqual(net_minutes(20, 12, 7, 60, 30), 10)

    def test_high_scenario(self):
        self.assertEqual(net_minutes(60, 12, 7, 60, 30), 210)

    def test_20_percent(self):
        self.assertAlmostEqual(affected_share(32, 160), 20.0)

    def test_curriculum_affected_credit_share(self):
        self.assertAlmostEqual(affected_share(43, 172), 25.0)

    def test_zero_total_rejected(self):
        with self.assertRaises(ValueError):
            affected_share(2, 0)

    def test_affected_more_than_total_rejected(self):
        with self.assertRaises(ValueError):
            affected_share(11, 10)

if __name__ == "__main__":
    unittest.main()
