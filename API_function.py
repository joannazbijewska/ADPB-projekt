# -*- coding: utf-8 -*-

"""
__author__ = "Joanna Zbijewska"
"""

import sys

class RNA_API():
    """RNA_API is a class to combine two API classes for downloading RNA structures and sequneces."""

    def __init__(self, database, what, inpt, input_type = None):
        self.db = database
        self.what = what
        self.inpt = inpt
        self.type = input_type

    def choose_db(self):
        db = self.db
        db = db.upper()
        if self.type is None:
            if db == "NDB":
                c = via_sequence(sequence = self.inpt)
            elif db == "RNA-STRAND" or db == "RNA-STRAND":
                c = RNA_STRAND(self.inpt)
            else:
                sys.stderr.write("Error: Invalid database name.")
                sys.exit(1)
        elif self.type.lower() == "pdb_id":
            c = Nucleic_acid_database(self.inpt)
        else:
            sys.stderr.write("Error: Invalid input type.")
            sys.exit(1)
        return(c)

    def use_API(self):
        if what == "sequence":
            c.download_fasta_sequence()
        elif what == "structure":
            if type(c) == "RNA_STRAND":
                c.download_bpseq_structure()
            else:
                c.download_pdb_structure()
        else:
            sys.stderr.write("Error: Invalid recquired output.")

#Przyklad uzycia:
#x = RNA_API("ndb","sequence","5SWE")
#x.use_API()
