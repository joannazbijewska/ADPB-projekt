# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:19:28 2016

@author: michalkarlicki
"""
import xlrd
import csv
import urllib
import requests
from lxml import html



class Service():
    def __init__(self, urldb):
        self.url = url

class Nucleic_acid_database():

    _urldb = "http://ndbserver.rutgers.edu"


    def __init__(self, pdb_id):
        self.pdb_id = pdb_id

    def data_base_download(self):
        url ="http://ndbserver.rutgers.edu"
        url1 = url+"/service/ndb/atlas/gallery/rna?polType=onlyRna&rnaFunc=all&protFunc=all&strGalType=rna&expMeth=all&seqType=all&galType=table&start=0&limit=50"
        query = requests.get(url1)
        tree = html.fromstring(query.content)
        link_do_bazy = tree.xpath('//tr/td/h2/span/a[@id]/@href')
        urllib.urlretrieve(url+link_do_bazy[0], "Documents/aktualna_baza.xls")

        #url = "http://ndbserver.rutgers.edu/sessions/2c72e2ca66ef2c8cf2ddec7502c9204089715776/Result.xls"
        #urllib.urlretrieve(url, "Documents/baza.xls")

    def csv_from_excel():
        wb = xlrd.open_workbook('Documents/baza.xls')
        sh = wb.sheet_by_name('sheet_1')
        your_csv_file = open('Documents/Result.csv', 'wb')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in xrange(sh.nrows):
            wr.writerow(sh.row_values(rownum))
        your_csv_file.close()

        csv_from_excel()
    def czytanie_bazy(self):
        with open("Documents/Result.csv","r") as f:
            otw = csv.reader(f)
            for i in otw:
                if i[1] == self.pdb_id:
                    return i
    def pdb_download(self):
        urldb = "http://ndbserver.rutgers.edu"
        pdb_id = self.pdb_id.lower()
        url1 = urldb+"/files/ftp/NDB/coordinates/na-nmr/pdb{}.ent.gz.".format(pdb_id)
        url2 = urldb+"/files/ftp/NDB/coordinates/na-biol/{}.pdb1".format(pdb_id)
        r = requests.get(url1)
        if r.status_code != 404:
            urllib.urlretrieve(url1, "Documents/{}.ent.gz.".format(pdb_id))
        else:
            urllib.urlretrieve(url2, "Documents/{}.pdb1".format(pdb_id))
        print "Sciaganie pliku pdb ".format(pdb_id)

    def view_sequence(self):
        urldb = "http://ndbserver.rutgers.edu"
        url = urldb+"/service/ndb/atlas/summary?searchTarget={}".format(self.pdb_id)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        sequence = tree.xpath('//p[@class="chain"]/text()')
        return sequence[0]

    def tworznie_raportu(self):
        csv_from_excel()
        plik = open("Documents/raport_{}".format(self.pdb_id), "w")
        plik.write("Rna z numeru pdb {}\n".format(self.pdb_id))
        Info_bazy = czytanie_bazy(pdb)
        for i in xrange(len(Info_bazy)):
            plik.write(Info_bazy[i]+"\n")
        view_sequence(pdb)
        pdb_download(pdb)
        print "Zapisano plik pdb w folderze Documents"
        print "Raport{}".format(self.pdb_id)
        plik.close()


#pdb_download("5KMZ")
#print czytanie_bazy("5KMZ")
#print view_sequence("5KMZ")
a = Nucleic_acid_database("5KMZ")
print a.czytanie_bazy()
