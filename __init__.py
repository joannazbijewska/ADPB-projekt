"""ADPB"""
print "module prettytable is needed"

from RNA_structure import API_NDB
from RNA_structure import API_RNA_STRAND
import os
#import subprocess
#import RNA_API
#import RBP_score
from subprocess import Popen, PIPE


def rmsd_calculation(x, y):
    """ Enter two pdb files """
    #os.system("python calculate_rmsd "+x+" "+y)
    cmd = "python calculate_rmsd "+x+" "+y
    #status = subprocess.call("python calculate_rmsd "+x+" "+y, shell=True)
    p = Popen(cmd, shell=True, stdout=PIPE)
    out, err = p.communicate()
    return (out,err)
    #print subprocess.check_call(status)
    #out = subprocess.check_output("Normal RMSD", "Kabsch RMSD")
    #return out

a = rmsd_calculation("5swe_TEST.pdb", "5swe_TEST.pdb")
print a
