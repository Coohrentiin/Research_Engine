"""
Test To Fraction written by Corentin Soubeiran
"""

__author__ = "Clement Caporal"

import ToFractions
import unittest

class KnownValues(unittest.TestCase):
    knownValues = (
        (1, 2, '+1/2'),
        (2, 4, '+1/2'),
        (-1, 4, '-1/4'),
        (1000, 1000, "+1/1")
    )


    def testToFraction(self):
        """ToFraction should give known result with known input"""
        for numerator, denumerator, string in self.knownValues:
            print('Testing KnownValues: {} {}'.format(numerator, denumerator))
        for numerator, denumerator, string in self.knownValues:
            result = ToFractions.fractions(numerator, denumerator).Fraction
            self.assertEqual(string, result)

class ToFractionsBadInput(unittest.TestCase):
    def testDivisonByZero(self):
        """ToFraction should fail with division by zero"""
        self.assertRaises(ToFractions.DivisionBy0, ToFractions.fractions,  1, 0)
    def testDenumeratorNotInteger(self):
        """ToFraction should fail with division by zero"""
        self.assertRaises(ToFractions.TypeErrore, ToFractions.fractions, 1, 1.9)
    def testNumeratorNotInteger(self):
        """ToFraction should fail with division by zero"""
        self.assertRaises(ToFractions.TypeErrore, ToFractions.fractions, 1.6, 2)

if __name__ == "__main__":
    unittest.main()
