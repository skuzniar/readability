import os
import sys

from formulas.AutomatedReadabilityIndex   import level as ari_level 
from formulas.FleschReadingEaseScore      import score as fre_score
from formulas.GunningFogIndex             import level as gfi_level
from formulas.FleschKincaidGradeLevel     import level as fkg_level
from formulas.ColemanLiauReadabilityIndex import level as clr_level
from formulas.SMOGIndex                   import level as smo_level
from formulas.OriginalLinsearWriteFormula import score as olf_score

class Runner:
    def load(self, path):
        with open(path, 'r') as file:
            return file.read()

    def run(self, path, formula, details, verbose):
        print("Running [%s]" % path)
        text = self.load(path)

        if (formula == 'ari' or formula == '*'):
            print("   Automated Readability Index Grade level ={:6.2f}".format(ari_level(text, details, verbose)))
        if (formula == 'fre' or formula == '*'):
            print("                 Flesch Reading Ease score ={:6.2f}".format(fre_score(text, details, verbose)))
        if (formula == 'gfi' or formula == '*'):
            print("             Gunning Fog Index Grade level ={:6.2f}".format(gfi_level(text, details, verbose)))
        if (formula == 'fkg' or formula == '*'):
            print("                Flesch-Kincaid Grade level ={:6.2f}".format(fkg_level(text, details, verbose)))
        if (formula == 'clr' or formula == '*'):
            print("Coleman-Liau Readability Index Grade level ={:6.2f}".format(clr_level(text, details, verbose)))
        if (formula == 'smo' or formula == '*'):
            print("                    SMOG Index Grade level ={:6.2f}".format(smo_level(text, details, verbose)))
        if (formula == 'olf' or formula == '*'):
            print("      Original Linsear Write Formula score ={:6.2f}".format(olf_score(text, details, verbose)))

