import bde
import unittest

class Knownvalues(unittest.TestCase):
    known_values_mail= ( ("Caporal","Clement",  "clement.caporal@ensta-paristech.fr"),
                         ("Caporal","Clément", "clement.caporal@ensta-paristech.fr"),
                         ("Haro","Pierre","pierre.haro@ensta-paristech.fr"),
                         ("De Kocker","Camille","camille.dekocker@ensta-paristech.fr"),
                         ("De Kocker","Camille","camille.de-kocker@ensta-paristech.fr"))
    known_values_whois=( ("Pioch","Romain","Secrétaire général"),
                         ("Pioch","Romain","Secretaire General"),
                         ("Soubeiran","corentin","Trésorier"))
    known_values_respo=( ("Présidante","Legrand"),
                         ("Vice Trésorier","Carpentier"))                      

    def test_mail(self):
        for firstname, lastname, mail in self.known_values_mail:
            result=bde.toENSTAEmail(firstname, lastname)
            self.assertEqual(mail,result)

    def test_whois(self):
        for firstname, lastname, statue in self.known_values_whois:
            result=bde.whoIs(firstname, lastname)
            self.assertEqual(statue,result)

    def test_respo(self):
        for statut,firstname in self.known_values_respo:
            result=bde.findRespo(statut)
            self.assertEqual(firstname,result)

class ToBdeBadInput(unittest.TestCase):
    def testBadType(self):
        for s in (("sdfze",0),(56,"zdfze"),(True,"sdg"),("sdfg0",False)):
            self.assertRaises(bde.NotStringError, bde.toENSTAEmail, s[0], s[1])

if __name__ == '__main__':
    unittest.main()