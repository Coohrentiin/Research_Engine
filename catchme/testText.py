# -*- coding: utf-8 -*-
#!/usr/local/bin/python3.4

"""
Test Index
"""
import os,sys,inspect
import unittest
import os
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
srcdir = currentdir + "/src"
print(srcdir)
sys.path.insert(0,srcdir) 
import text

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
        for tex, result in self.knownSplitValues:
            self.assertEqual(text.get_occurency(tex.split()), result)
    
    def testCleanText(self):
        for tex, result in self.knownCleanValues:
            self.assertEqual(text.clean_text(tex), result)

if __name__ == "__main__":
    unittest.main()
