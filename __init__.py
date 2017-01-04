"""ADPB"""
print "module prettytable is needed"

import API_PROJEKT
#import API_RNA_STRAND
import os

def rmsd_calculation(x, y):
    """ Enter two pdb files """
    os.system("python calculate_rmsd "+x+" "+y)


rmsd_calculation("5swe.pdb", "5swe.pdb")
