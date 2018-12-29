# coding:utf-8
import unittest
from case.F2_test import F2


class Runmain:
    def __init__(self):
        pass

    @staticmethod
    def run_case():
        suite = unittest.TestSuite()
        suite.addTests(map(F2, ["test_11order_submit", "test_12reject"]))
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    run = Runmain()
    run.run_case()
