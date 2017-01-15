# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:19:28 2016

___author__: "Michal Karlicki, Gruszka, Asia Zbijewska"
"""
import xlrd
import csv
import urllib
import requests
from lxml import html
import re
import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio import SeqIO

def csv_from_excel():
    """Xls files converter"""
    wb = xlrd.open_workbook('NDB_updated.xls')
    sh = wb.sheet_by_name('sheet_1')
    your_csv_file = open('NDB_database.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    your_csv_file.close()

def database_read(pdb_id):
    """Database reader"""
    with open("NDB_database.csv","r") as f:
        otw = csv.reader(f)
        for i in otw:
            if i[1] == pdb_id:
                return i


def search_blast_pdb(sequence):
    """Searching through the database using desired sequence"""
    urldb = "http://www.rcsb.org/pdb/rest"
    url = urldb+"/getBlastPDB1?sequence={}&eCutOff=10.0&matrix=BLOSUM62&outputFormat=html".format(sequence)
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

def check_base(pdb_id):
    with open("NDB_database.csv","r") as f:
        otw = csv.reader(f)
        for i in otw:
            if i[1] == x:
                return True
            else:
                return "No records found"

def get_from_db_via_seq(sequence):
    pdb_ids = search_blast_pdb(sequence) #zakładając pierwszy jako właściwy
    for i in pdb_ids:
        if check_base(i) is True:
            return i
        else:
            return sequence[0]



class Nucleic_acid_database():
    """This class serves to access NDB database, download it, search it and download single files"""
    _urlna = "http://ndbserver.rutgers.edu"

    def __init__(self, pdb_id):
        self.pdb_id = pdb_id

    def download_database(self):
        """Database updater"""
        url ="http://ndbserver.rutgers.edu"
        url1 = url+"/service/ndb/atlas/gallery/rna?polType=onlyRna&rnaFunc=all&protFunc=all&strGalType=rna&expMeth=all&seqType=all&galType=table&start=0&limit=50"
        query = requests.get(url1)
        tree = html.fromstring(query.content)
        database_link = tree.xpath('//tr/td/h2/span/a[@id]/@href')
        urllib.urlretrieve(url+database_link[0], "NDB_updated.xls")
        csv_from_excel()
        return "NDB Database was updated and converted to csv file"

    def database_read_metadata(self):
        """Metadata reader """
        with open("NDB_database.csv","r") as f:
            otw = csv.reader(f)
            for i in otw:
                if i[1] == self.pdb_id:
                      meta = i

        return "Pdb id: {pdb}\nNbd id: {nbd}\nName of the structure: {nazwa}\nTitle of the publication: {title}\nDate of publication: {data}\nAuthors: {aut}\nMethod: {method}\nResolution: {rez}\nR value: {rvl}".format(pdb = meta[1], nazwa = meta[3], nbd = meta[0], title = meta[6], data = meta[4], aut = meta[5], method = meta[8], rez = meta[9], rvl = meta[10])

    def download_pdb_structure(self):
        """Structure downloader in pdb format"""
        urldb = "http://ndbserver.rutgers.edu"
        pdb_id = self.pdb_id.lower()
        url1 = urldb+"/files/ftp/NDB/coordinates/na-nmr/pdb{}.ent.gz.".format(pdb_id)
        url2 = urldb+"/files/ftp/NDB/coordinates/na-biol/{}.pdb1".format(pdb_id)
        r = requests.get(url1)
        if r.status_code != 404:
            urllib.urlretrieve(url1, "{}.ent.gz.".format(pdb_id))
        else:
            urllib.urlretrieve(url2, "{}.pdb1".format(pdb_id))
        os.rename(pdb_id+".pdb1", pdb_id+".pdb")
        return "PDB file {} is ready".format(pdb_id.upper())


    def get_seq_record(self):
        """Sequence viewer for desired PDB ID"""
        urldb = "http://ndbserver.rutgers.edu"
        pdb_id = self.pdb_id
        url = urldb+"/service/ndb/atlas/summary?searchTarget={}".format(pdb_id)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        sequence = tree.xpath('//p[@class="chain"]/text()')
        with open("NDB_database.csv","r") as f:
            opened = csv.reader(f)
            for i in opened:
                if i[1] == pdb_id:
                    meta = i
        record = SeqRecord(Seq(sequence[0],IUPAC.ambiguous_rna), id=pdb_id, name = "RNA sequence", description=meta[3])
        return record

    def download_fasta_sequence(self):
        """Sequence download in fasta format for desired PDB ID"""
        pdb_id = self.pdb_id
        sequence = self.get_seq_record()
        with open("{}_sequence.fasta".format(pdb_id),"w") as f:
            SeqIO.write(sequence, f, "fasta")
        return "Fasta file is ready"

    def metadata_to_file(self):
        """Metadata download for specified sequence or PDB ID"""
        pdb_id = self.pdb_id
        with open("NDB_database.csv","r") as f:
            otw = csv.reader(f)
            for i in otw:
                if i[1] == pdb_id:
                      meta = i
        f = open("report_{}".format(pdb_id), "w")
        metadata = "Pdb id: {pdb}\nNbd id: {nbd}\nName of the structure: {nazwa}\nTitle of the publication: {title}\nDate of publication: {data}\nAuthors: {aut}\nMethod: {method}\nResolution: {rez}\nR value: {rvl}".format(pdb = meta[1], nazwa = meta[3], nbd = meta[0], title = meta[6], data = meta[4], aut = meta[5], method = meta[8], rez = meta[9], rvl = meta[10])
        f.write("RNA structure from NBD\n"+metadata)
        f.close()
        return "File with metadata is ready"

    def metadata(self):
        """Unable to view metadata for specified sequence or PDB ID"""
        with open("NDB_database.csv","r") as f:
            pdb_id = self.pdb_id
            opened = csv.reader(f)
            for i in opened:
                if i[1] == pdb_id:
                    meta = i
            information = "Pdb id: {pdb}\nNbd id: {nbd}\nName of the structure: {nazwa}\nTitle of the publication: {title}\nDate of publication: {data}\nAuthors: {aut}\nMethod: {method}\nResolution: {rez}\nR value: {rvl}".format(pdb = meta[1], nazwa = meta[3], nbd = meta[0], title = meta[6], data = meta[4], aut = meta[5], method = meta[8], rez = meta[9], rvl = meta[10])
            return information

class via_sequence(Nucleic_acid_database):
    """This class inherites form the Nucleic_acid_database class and enables searching and downloading
    from NDB database via sequence"""

    def __init__(self, sequence = None, pdb_id = None):
        self.sequence = sequence
        if pdb_id is None:
            self.pdb_id = get_from_db_via_seq(self.sequence)
        else:
            self.pdb_id = pdb_id



#proba = via_sequence(pdb_id = "5SWE")
#print proba.download_fasta_sequence()
