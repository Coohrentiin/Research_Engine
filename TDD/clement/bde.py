"""
bde.py gives automated result for existential question in the ENSTA student union.
"""

__author__ = "Clement caporal"
__license__ = "Python"

#Define exceptions
class BdeError(Exception): pass
class NotStringError(BdeError): pass


#Define Name Mapping
bdeTrombinoscopeMap = [["Legrand", "Emeline", "Presidente"],
                    ["Haro", "Pierre", "Vice President"],
                    ["Pioch", "Romain", "Secretaire General"],
                    ["Soubeiran", "Corentin", "Tresorier"],
                    ["Carpentier", "Antoine", "Vice tresorier"],
                    ["Hasbini", "Laura", "Respo Association"],
                    ["Caporal", "Clement", "Respo Alumni"],
                    ["Kobayashi", "Victor", "Respo AST"],
                    ["Leignel", "Hortense", "Respo Scolarite"],
                    ["Lefort", "Alberic", "Respo Scolarite"],
                    ["Aujoux", "Clarisse", "Respo Communication"],
                    ["De Kocker", "Camille", "Respo Presse"],
                    ["Boyer", "Thomas", "Respo Relations Exterieures"],
                    ["Gomez", "Louis", "Respo Relations Exterieures"],
                    ["Pelletier", "Erwan", "Respo WEI"],
                    ["Xu", "Lucia", "Respo Entreprises"],
                    ["Gardon", "Pierre", "Respo Entreprises"],
                    ["Van Der Beek", "Bruno", "Respo Entreprises"]]


def toENSTAEmail(first_name, last_name):
    """convert first_name and last_name to ENSTA Email"""
    if type(first_name) != str or type(last_name) != str:
        raise NotStringError
    return first_name.replace(" ", "-").lower() + "." + last_name.replace(" ", "-")lower() + "@ensta-paristech.fr"

def findRespo(respo):
    """find the names of the person in charge of the BDE for a given project"""
    respo_names = []
    for pers in bdeTrombinoscopeMap:
        if respo in pers[2]:
            respo_names.append(pers[0])
    return respo_names

def whoIs(first_name, last_name):
    """find the charge of the person"""
    for pers in bdeTrombinoscopeMap:
        if first_name == pers[1]:
            if last_name == pers[0]:
                return pers[2]
    return "This person has no charge in BDE"