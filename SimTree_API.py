# -*- coding: utf-8 -*-

"""
Serves as application programmers interface for browser tool SimTree.
Enables user to compare two RNA secondary structures in dot-parentheses format.
by: Joanna Zbijewska <asia.zbijewska@gmail.com>
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import sys

class SimTree():
    """SimTree class serves to access and use SimTree web tool"""

    def __init__(self, dot_parentheses_1, dot_parentheses_2):
        self.struct1 = dot_parentheses_1
        self.struct2 = dot_parentheses_2

    def choose_browser(self):
        """Choosing browser of use enables adjusting the script for your browser
        Input must be a string specifying browser name all in small letters without special characters"""
        browser_name = input("Type your browser name here: ")
        possible_browsers = ["firefox","internetexplorer","chrome"]
        if not browser_name == any(browser) for browser in possible_browsers:
            sys.stderr.write("Error: We currently don't support your browser type.")
            sys.exit(1)
        else:
            if browser_name == "chrome":
                driver = webdriver.Chrome()
            elif browser_name == "internetexplorer":
                driver = webdriver.Ie()
            else:
                driver = webdriver.Firefox()
        return(driver)

    def enter_simtree(self):
        """Enters SimTree tool webpage and identifies recquired input elements"""
        driver = self.choose_browser()
        driver.get("http://bioinfo.cs.technion.ac.il/SimTree/")
        input_1_type = driver.find_element(By.NAME, "seq1inType")
        select_input_1_type = Select(input_1_type)
        select_input_1_type.select_by_visible_text(" Parentheses ")
        input_2_type = driver.find_element(By.NAME, "seq2inType")
        select_input_2_type = Select(input_2_type)
        select_input_2_type.select_by_visible_text(" Parentheses ")

    def paste_sequences(self):
        """Serves to paste the desired structures in dot-parentheses format into
        specified text areas"""
        self.enter_simtree()
        driver = self.choose_browser()
        area_1 = driver.find_element(By.NAME, "seq1")
        area_1.send_keys("{}".format(self.struct1))
        area_2 = driver.find_element(By.NAME, "seq2")
        area_2.send_keys("{}".format(self.struct2))

    def compare(self):
        """Submits two structures for comparison"""
        self.paste_sequences()
        driver = self.choose_browser()
        driver.find_element_by_xpath("//input[@type='submit']").click()
