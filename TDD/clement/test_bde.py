import bde
import unittest

class Knownvalues(unittest.TestCase):
    known_values_mail= ( ("Caporal","Clement",  "clement.caporal@ensta-paristech.fr"),
                         ("Caporal","Clément", "clement.caporal@ensta-paristech.fr"),
                         ("Haro","Pierre","pierre.haro@ensta-paristech.fr"),
                         ("De Kocker","Camille","camille.dekocker@ensta-paristech.fr"),
                         ("De Kocker","Camille","camille.de-kocker@ensta-paristech.fr"))
    known_values_whois=( ("Pioch","Romain","SexGé"),
                         ("Pioch","Romain","Secretaire General"),
                         ("Soubeiran","corentin","Trésorier"))
    known_values_respo=( ("Présidante","Legrand"),
                         ("Vice Trésorier","Carpentier"))                      

    def test_mail(self):
        for firstname, lastname, mail in self.known_values_mail:
            result=bde.toENSTAEmail(firstname, lastname)
            self.assertEqual(mail,result)

if __name__ == '__main__':
    unittest.main()