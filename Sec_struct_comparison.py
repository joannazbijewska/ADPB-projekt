import re

class BPSEQ():
    """docstring for ."""

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

    def bp_distance(self):
        pairs_indices = self.bpseq_pairs()
        pairs = {}
        for key in pairs_indices:
            value = pairs_indices[key]
            if not value=='0':
                pairs[key] = value
        

a = BPSEQ('PDB_01121_structure')
a.bp_distance()
