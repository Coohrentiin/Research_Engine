"""
Test Index
"""

import src.text
import unittest
import os

class KnownValues(unittest.TestCase):
    knownSplitValues = (
        ("What is a banana in a night banana", {'What': 1, 'is': 1, 'a': 2, 'banana': 2, 'in': 1, 'night': 1}),
        ("Superman", {"Superman": 1}),
        ("Je çui francé", {"Je": 1, "çui":1, "francé":1}),
        ("", {})
    )
    
    knownCleanValues = (
        ("What is a banana in a night banana", ["banana", "night", "banana"]),
        ("", []),
        ("Je çui francéàû", ["je", "çui", "francéàû"]),
        ("making,   .. https:// * www <>\n'()resolving-(') _ resolved", ["make", "http", "www", "resolv", "_", "resolv"])
    )

    def testGetOccurency(self):
        """Should return occurences of words in a text"""
        for text, result in self.knownSplitValues:
            self.assertEqual(src.text.get_occurency(text.split()), result)
    
    def testCleanText(self):
        for text, result in self.knownCleanValues:
            self.assertEqual(src.text.clean_text(text), result)

if __name__ == "__main__":
    unittest.main()
