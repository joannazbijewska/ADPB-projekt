# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:19:28 2016

@author: michalkarlicki, gruszka, asiazbijewska
"""
import xlrd
import csv
import urllib
import requests
from lxml import html
import re


def search_blast_pdb(x):
    urldb = "http://www.rcsb.org/pdb/rest"
    url = urldb+"/getBlastPDB1?sequence={}&eCutOff=10.0&matrix=BLOSUM62&outputFormat=html".format(x)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    sequence = tree.xpath('//pre/pre/text()')
    pattern = "([A-Z,0-9])\w+"
    list_pdb_id = []
    for i in sequence:
        match = re.search(pattern, i)
        if match:
            if len(match.group(0)) == 4:
                list_pdb_id.append(match.group(0))
    if len(list_pdb_id) > 3:
        return list_pdb_id[0:3]
    else:
        return list_pdb_id

def check_base(x):
    with open("data_base.csv","r") as f:
        otw = csv.reader(f)
        for i in otw:
            if i[1] == x:
                return True




class Nucleic_acid_database():

    _urldb = "http://ndbserver.rutgers.edu"

    def csv_from_excel(self):
        wb = xlrd.open_workbook('NDB_updated.xls')
        sh = wb.sheet_by_name('sheet_1')
        your_csv_file = open('NDB_database.csv', 'wb')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in xrange(sh.nrows):
            wr.writerow(sh.row_values(rownum))
        your_csv_file.close()

    def __init__(self, pdb_id):
        self.pdb_id = pdb_id

    def download_database(self):
        url ="http://ndbserver.rutgers.edu"
        url1 = url+"/service/ndb/atlas/gallery/rna?polType=onlyRna&rnaFunc=all&protFunc=all&strGalType=rna&expMeth=all&seqType=all&galType=table&start=0&limit=50"
        query = requests.get(url1)
        tree = html.fromstring(query.content)
        database_link = tree.xpath('//tr/td/h2/span/a[@id]/@href')
        urllib.urlretrieve(url+database_link[0], "NDB_updated.xls")
        #url = "http://ndbserver.rutgers.edu/sessions/2c72e2ca66ef2c8cf2ddec7502c9204089715776/Result.xls"
        #urllib.urlretrieve(url, "Documents/baza.xls")

    def database_read(self):
        with open("Documents/NDB_database.csv","r") as f:
            otw = csv.reader(f)
            for i in otw:
                if i[1] == self.pdb_id:
                    return i

    def structure_download(self):
        urldb = "http://ndbserver.rutgers.edu"
        pdb_id = self.pdb_id.lower()
        url1 = urldb+"/files/ftp/NDB/coordinates/na-nmr/pdb{}.ent.gz.".format(pdb_id)
        url2 = urldb+"/files/ftp/NDB/coordinates/na-biol/{}.pdb1".format(pdb_id)
        r = requests.get(url1)
        if r.status_code != 404:
            urllib.urlretrieve(url1, "Documents/{}.ent.gz.".format(pdb_id))
        else:
            urllib.urlretrieve(url2, "Documents/{}.pdb1".format(pdb_id))
        print "PDB file download...".format(pdb_id)

    def sequence_view(self):
        urldb = "http://ndbserver.rutgers.edu"
        url = urldb+"/service/ndb/atlas/summary?searchTarget={}".format(self.pdb_id)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        sequence = tree.xpath('//p[@class="chain"]/text()')
        return sequence[0]

    def report_creator(self):
        csv_from_excel()
        f = open("Documents/report_{}".format(self.pdb_id), "w")
        f.write("RNA from PDB ID {}\n".format(self.pdb_id))
        base_info = database_read(pdb)
        for i in xrange(len(base_info)):
            f.write(base_info[i]+"\n")
        sequence_view(pdb)
        structure_download(pdb)
        print "PDB file saved in Documents folder"
        print "Report{}".format(self.pdb_id)
        f.close()

#<<<<<<< HEAD
class via_sequence(Nucleic_acid_database):
    def __init__(self, sequence, pdb_id = None):
        self.sequence = sequence

    def get_from_db_via_seq(self):
        pdb_ids = search_blast_pdb(self.sequence) #zakładając pierwszy jako właściwy
        for i in pdb_ids:
            if check_base(i) is True:
                return i
            else:
                return sequence[0]
szukamy = via_sequence("AACCUUCACCAAUUAGGUUCAAAUAAGUGGU")
print szukamy.get_from_db_via_seq()
#=======

#pdb_download("5KMZ")
#print czytanie_bazy("5KMZ")
#print view_sequence("5KMZ")
a = Nucleic_acid_database("5KMZ")
print search_blast_pdb(a.sequence_view())

class RNA_STRAND():
    _urldb = "http://www.rnasoft.ca/strand/"


#>>>>>>> joannazbijewska/master
