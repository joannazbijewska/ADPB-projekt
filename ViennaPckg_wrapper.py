
import os
import sys

from __future__ import print_function

from Bio.Application import _Option, _Switch, AbstractCommandline

class RNA2Dfold(AbstractCommandline):
    def __init__(self, cmd=None, **kwargs):
        assert cmd is not None
        extra_parameters = [
            _Switch(["-h","-−help", "help"],
                    "Print help and exit"),
            _Switch(["−−detailed−help","detailed"]
                    "Print help, including all details and hidden options, and exit"),
            _Switch(["-V", "−−version","version"]
                    "Print version and exit"),
#General Options:
            _Switch(["−−noconv","noconv"]
                    "Do not automatically substitude nucleotide "T" with "U".
                    (default=off)"),
            _Switch(["−−noconv","noconv"]
                    "Do not automatically substitude nucleotide "T" with "U"."),
            ]
        try:
            # Insert extra parameters - at the start just in case there
            # are any arguments which must come last:
            self.parameters = extra_parameters + self.parameters
        except AttributeError:
            # Should we raise an error?  The subclass should have set this up!
            self.parameters = extra_parameters
        AbstractCommandline.__init__(self, cmd, **kwargs)
"""
−j, −−numThreads=INT

Set the number of threads used for calculations (only available when compiled with OpenMP support)

Algorithms:
−p, −−partfunc

calculate partition function and thus, Boltzmann probabilities and Gibbs free energy

(default=off)

−−stochBT=INT

backtrack a certain number of Boltzmann samples from the appropriate k,l neighborhood(s)

−−neighborhood=<k>:<l>

backtrack structures from certain k,l−neighborhood only, can be specified multiple times (<k>:<l>,<m>:<n>,...)

−S, −−pfScale=DOUBLE

scaling factor for pf to avoid overflows

−−noBT

do not backtrack structures, calculate energy contributions only

(default=off)

−c, −−circ

Assume a circular (instead of linear) RNA molecule.

(default=off)

Model Details:
−T, −−temp=DOUBLE

Rescale energy parameters to a temperature of temp C. Default is 37C.

−K, −−maxDist1=INT

maximum distance to first reference structure

If this value is set all structures that exhibit a basepair distance greater than maxDist1 will be thrown into a distance class denoted by K=L=−1

−L, −−maxDist2=INT

maximum distance to second reference structure

If this value is set all structures that exhibit a basepair distance greater than maxDist1 will be thrown into a distance class denoted by K=L=−1

−4, −−noTetra

Do not include special tabulated stabilizing energies for tri−, tetra− and hexaloop hairpins. Mostly for testing.

(default=off)

−P, −−parameterFile=paramfile Read energy parameters from paramfile,
instead

of using the default parameter set.

A sample parameter file should accompany your distribution. See the RNAlib documentation for details on the file format.

−d, −−dangles=INT

How to treat "dangling end" energies for bases adjacent to helices in free ends and multi−loops

(possible values="0", "2" default=‘2’)

With −d2 dangling energies will be added for the bases adjacent to a helix on both sides

in any case.

The option −d0 ignores dangling ends altogether (mostly for debugging).

−−noGU

Do not allow GU pairs

(default=off)

−−noClosingGU

Do not allow GU pairs at the end of helices

(default=off)"""
