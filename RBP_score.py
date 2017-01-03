# -*- coding: utf-8 -*-

"""
Calculate relaxed base pair score or simply base pair score between two structures
saved in bpseq format.
by: Joanna Zbijewska <asia.zbijewska@gmail.com>
"""

import re
import math

class BPSEQ():
    """This class serves to parse the bpseq file format of
    RNA secondary structure to get the base indices and base pairs"""

    def __init__(self, filename):
        self.filename = filename

    def bpseq_input(self):
        data = []
        with open("{}.bpseq".format(self.filename),"r") as sec_struct:
            sec_structure = sec_struct.readlines()
            for line in sec_structure:
                data.append(line)
        sec_struct.close()
        new_data=[]
        for element in data:
            new_data.append(element.strip('\n'))
        list_of_lists = []
        for element in new_data:
            test = '([0-9])\w+'
            if re.match(test,element):
                list_of_lists.append(element.split(' '))
        return(list_of_lists)

    def bpseq_indices(self):
        list_of_lists = self.bpseq_input()
        base_indices = {}
        for i in range(len(list_of_lists)):
            alist = list_of_lists[i]
            base_indices[alist[0]] = alist[1]
        return(base_indices)

    def bpseq_pairs(self):
        list_of_lists = self.bpseq_input()
        pair_indices = {}
        for i in range(len(list_of_lists)):
            alist = list_of_lists[i]
            pair_indices[alist[0]] = alist[2]
        return(pair_indices)

class struct_comparison():
    """This class takes two filenames of structures in bpseq format
    to compare."""

    def __init__(self, filename1, filename2):
        self.1 = filename1
        self.2 = filename2

    def initialize(self):
    """This function prepares structures to compare using the BPSEQ class"""
        #Czy ja w ogole moge tak zrobic? Czy to zadziala?
        one = BPSEQ(self.1)
        two = BPSEQ(self.2)
        one = one.bpseq_pairs()
        two = two.bpseq_pairs()
        return(list(one, two))

    def bp_distances(self):
        pairs_from_two = self.initialize()
        one_1 = []
        one_2 = []
        two_1 = []
        two_2 = []
        for key in pairs_from_two[0]:
            one_1.append(key)
        for value in pairs_from_two[0]:
            one_2.append(value)
        for key in pairs_from_two[1]:
            two_1.append(key)
        for value in pairs_from_two[1]:
            two_2.append(value)
        list_of_distances_1 = []
        list_of_distances_2 = []
        for n in range(len(one_1)):
            temp = []
            for i in range(len(two_1)):
                temp.append(max((int(one_1[n])-int(two_1[i])),(int(one_2[n])-int(two_2[i]))))
            list_of_distances_1.append(temp)
        for n in range(len(two_1)):
            temp = []
            for i in range(len(one_1)):
                temp.append(max((int(two_1[n])-int(one_1[i])),(int(two_2[n])-int(one_2[i]))))
            list_of_distances_2.append(temp)
        return(list(list_of_distances_1,list_of_distances_2))

    def bp_score(self):
        """Returns a list of distances between baise pairs (for nonzero distances) in two given structures"""
        list_bp_distances = self.bp_distances()
        score = []
        for part in list_bp_distances:
            for alist in part:
                score.append(min(alist))
        score.sort()
        return(score)

    def return_bp_score(self):
        """Returns the value of the base pair score - the old method of comparison
        for secondary RNA structures"""
        scores_list = self.bp_score()
        bp_score = len(scores_list)
        print('Your calculated base pare score is {}'.format(bp_score))

    def rbp_score(self):
        bp_score = self.bp_score()
        t = input('Choose your relaxation paramter: ')
        t = int(t)
        if t < 0:
            print("Wrong number. Relaxation parameter must be bigger than zero.")
            self.rbp_score()
        elif t == 0:
            self.return_bp_score()
        else:
            possible_m_vals = []
            for ind in range(len(bp_score)):
                min_m = bp_score[ind]/t
                min_m = math.floor(min_m)
                possible_m_vals.append(min_m)
        rbp_score = min(possible_m_vals)
        print('Your calculated relaxed base pare score for relaxation parameter t = {} is {}'.format(t,rbp_score))
