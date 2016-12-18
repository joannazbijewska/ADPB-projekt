
import unittest
import API_PROJEKT
import os


class API_PROJEKTfunctions(unittest.TestCase):

    def test_sequence_view(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.sequence_view()
        sequence = "GGGAAGAUAUAAUCCUAAUGAUAUGGUUUGGGAGUUUCUACCAAGAGCCUUAAACUCUUGAUUAUCUUCCC"
        self.assertEqual(result, sequence)

    def test_download_fasta_sequence(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.download_fasta_sequence()
        expected = "Sequence 5SWE is ready"
        self.assertEqual(result, expected)
        os.remove("plik_fasta_5SWE.fasta")

    def test_metadata_to_file(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.metadata_to_file()
        expected = "File with metadata is ready"
        self.assertEqual(result, expected)
        os.remove("report_5SWE")

    def test_structure_download(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.structure_download()
        expected = "PDB file 5SWE is ready"
        self.assertEqual(result, expected)
        os.remove("5swe.pdb1")
    def test_download_database(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.download_database()
        expected = " NDB Database was updated and converted to csv file"
        self.assertEqual(result, expected)

#class BiospamTestDivision(unittest.TestCase):

#    def test_division1(self):
#        result = Biospam.division(3.0, 2.0)
#        self.assertAlmostEqual(result, 1.5)

#    def test_division2(self):
#        result = Biospam.division(10.0, -2.0)
#        self.assertAlmostEqual(result, -5.0)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
