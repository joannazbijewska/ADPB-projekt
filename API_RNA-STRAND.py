# -*- coding: utf-8 -*-

"""
__author__ = "Asia Zbijewska, Gruszka"
"""

import re
import csv
import urllib
import requests
from lxml import html

class RNA_STRAND():
    _urlrna = "http://www.rnasoft.ca/strand/"

    def download_database(self):
        urlrna = "http://www.rnasoft.ca/strand/"
        url = urlrna+"download/RNA_STRAND_data.tar.gz"
        urllib.urlretrieve(url, "Downloads/RNA_STRAND_data.tar.gz")
        print "RNA STRAND database downloaded to Downloads folder."

    def __init__(self, sequence):
        self.sequence = sequence

    def fetch_by_sequence(self):
        urlrna = "http://www.rnasoft.ca/strand/"
        search = urlrna+"search_results.php?select%5B%5D=Any+type&org=&source%5B%5D=Any+source&source_id=&select2=Any+length&first1=&last1=&exp_proven=Any&select4=Any+number&first2=&last2=&select5=Any&select_duplicate=All+molecules&seq={}&abstractshapetype=ABSTRACT_SHAPE_5&abstractshape=&Submit=Perform+search&select6=Any+number&first3=&last3=&select7=Any+number&first4=&last4=&select8=Any+number&first5=&last5=&select12=Any+number&first7=&last7=&select13=Any+number&first8=&last8=&motif=&select19=Any+number&first10=&last10=&select20=Any+number&first11=&last11=&select25=Any+number&first13=&last13=&select26=Any+number&first14=&last14=&select27=absolute&select28=Any+number&first15=&last15=&select33=Any+number&first17=&last17=&select34=Any+number&first18=&last18=&select35=average&select36=absolute&select37=Any+number&first19=&last19=&select38=Any+number&first20=&last20=&select69=Any+number&first31=&last31=&select71=bands&select72=Any+number&first32=&last32=&select73=base+pairs&select74=Any+number&first33=&last33=&select75=Any&select76=Any+number&first34=&last34=&select55=any&select_ncbp_context_2=any&select_ncbp_context_4=any&select_ncbp_context_1=any&select_ncbp_context_5=any&select56=Any+number&first26=&last26=&start=0&limit=100&sort_by=length&order=ascending".format(self.sequence)
        found = requests.get(search)
        output = html.fromstring(found.content)
        output_list = output.xpath('//tr/td/text()')
        regex1 = re.compile(r'(Any)')
        regex2 = re.compile(r'(\n)')
        regex3 = re.compile(r'(\t)')
        regex4 = re.compile(r'(Unknown)')
        regex5 = re.compile(r'\[')
        regex6 = re.compile(r'(In all)')
        regex7 = re.compile(r'\ ')
        regex8 = re.compile(r'(Remove outliers)')
        regex9 = re.compile(r'(Normalize by RNA type)')
        out = [regex7,regex8,regex9]
        result1=[]
        for i in output_list:
            if regex1.search(i)==None:
                result1.append(i)
        result2=[]
        for i in result1:
            if regex2.search(i)==None:
                result2.append(i)
        result3=[]
        for i in result2:
            if regex3.search(i)==None:
                result3.append(i)
        result4=[]
        for i in result3:
            if regex4.search(i)==None:
                result4.append(i)
        result5=[]
        for i in result4:
            if regex5.search(i)==None:
                result5.append(i)
        result6=[]
        for i in result5:
            if regex6.search(i)==None:
                result6.append(i)
        result = [x for x in result6 if not any (regex.match(x) for regex in out)]
