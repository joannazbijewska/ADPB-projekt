from setuptools import setup

setup(name = "RNA_structures",
version = "0.5",
description = "This is the package serves to access the RNA databases, dowlnoad sequences and structures, predict and compare RNA structures.",
author = "Agata Gruszczynska, Michal Karlicki, Joanna Zbijewska",
author_email = "gruszczynska.agat@gmail.com,,asia.zbijewska@gmail.com",
license = "BSD-2-Clause",
packages = ["API_RNA_STRAND","RNA_NDB","RBP_score","API_function"],
install_recquires = ["biopython","prettytable","xlrd"])
