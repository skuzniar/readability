import os
import sys

from formulas.AutomatedReadabilityIndex   import level as ari_level 
from formulas.FleschReadingEaseScore      import score as fre_score
from formulas.GunningFogIndex             import level as gfi_level
from formulas.GunningFogIndex             import level_simple as gfi_level_s
from formulas.GunningFogIndex             import level_fast as gfi_level_f
from formulas.FleschKincaidGradeLevel     import level as fkg_level
from formulas.ColemanLiauReadabilityIndex import level as clr_level
from formulas.SMOGIndex                   import level as smo_level
from formulas.OriginalLinsearWriteFormula import score as olf_score

formulas = [
        ("ari", ari_level, "Automated Readability Index Level"),
        ("fre", fre_score, "Flesch Reading Ease Score"),
        ("gfi", gfi_level,   "Gunning Fog Index Level (remove suffix only if the stem is valid)"),
        ("gfi", gfi_level_f, "Gunning Fog Index Level (remove suffix even if the stem is invalid)"),
        ("gfi", gfi_level_s, "Gunning Fog Index Level (no suffix removal)"),
        ("fkg", fkg_level, "Flesch-Kincaid Grade Level"),
        ("clr", clr_level, "Coleman-Liau Readability Index Level"),
        ("smo", smo_level, "SMOG Index Level"),
        ("olf", olf_score, "Original Linsear Write Formula Score")]

class Runner:
    #--- Clients only get codes and descriptions
    def formulas(self):
        return [(c, d) for c, _, d in formulas]

    def load(self, path):
        with open(path, 'r') as file:
            return file.read()

    def run(self, path, code, details, verbose):
        codes = [c for c, _, _ in formulas]
        if code != '*' and not code in codes:
            print("Unknown code:", code)
            return

        print("Running [%s]" % path)
        text = self.load(path)

        selected = [element for element in formulas if element[0] == code or code == '*']
        for c, f, d in selected:
            print("{:>36} ={:6.2f}".format(d, f(text, details, verbose)))

