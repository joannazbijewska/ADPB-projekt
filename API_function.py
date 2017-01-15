# -*- coding: utf-8 -*-

"""
__author__ = "Joanna Zbijewska"
"""

import sys
import API_RNA_STRAND
import API_PROJEKT

class RNA_API():
    """RNA_API is a class to combine two API classes for downloading RNA structures and sequneces."""

    def __init__(self, database, what, inpt, input_type = None):
        """Four arguments:
        database: to choose the database you want to access
        what: to choose type of data you want to get - sequence or structure
        inpt: string to search through the database - a string for sequence or PDB id
        input_type: if the inpt string is a PDB id you have to type "pdb_id"
        """
        self.db = database
        self.what = what
        self.inpt = inpt
        self.type = input_type

    def choose_db(self):
        """Function to choose the database. It gives the class to inpt."""
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
        """Downloads sequence or structure depending on what value"""
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
