
import unittest
import API_PROJEKT
import API_RNA_STRAND
import os


class API_PROJEKTfunctions(unittest.TestCase):
    """ The internet connection is necessary  """
    def test_getsequence(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        #result = example.get_seq_record()
        assert example.get_seq_record() is not None
        #sequence = "GGGAAGAUAUAAUCCUAAUGAUAUGGUUUGGGAGUUUCUACCAAGAGCCUUAAACUCUUGAUUAUCUUCCC"
        #self.assertEqual(result, sequence)

    def test_download_fasta_sequence(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.download_fasta_sequence()
        expected = "Fasta file is ready"
        self.assertEqual(result, expected)
        os.remove("5SWE_sequence.fasta")

    def test_metadata_to_file(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.metadata_to_file()
        expected = "File with metadata is ready"
        self.assertEqual(result, expected)
        os.remove("report_5SWE")

    def test_structure_download(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.download_pdb_structure()
        expected = "PDB file 5SWE is ready"
        self.assertEqual(result, expected)
        os.remove("5swe.pdb")

    def test_download_database(self):
        example = API_PROJEKT.via_sequence(pdb_id = "5SWE")
        result = example.download_database()
        expected = "NDB Database was updated and converted to csv file"
        self.assertEqual(result, expected)

class ApiRNASTRANDfunctions(unittest.TestCase):

    def test_searchbysequence(self):
        example = API_RNA_STRAND.RNA_STRAND('UAAGCCCUA')
        #result = example.search_by_sequence()
        assert example.search_by_sequence() is not None

    def test_download_database(self):
        example = API_RNA_STRAND.RNA_STRAND('UAAGCCCUA')
        result = example.download_database()
        expected = "RNA STRAND database downloaded to Downloads folder."
        self.assertEqual(result, expected)
        os.remove("RNA_STRAND_data.tar.gz")
    #def test_searchbysequence(self):
    #    example = API_RNA_STRAND.RNA_STRAND('UAAGCCCUA')
       #result = example.search_by_sequence()
    #    assert example.choose_result() is not None
    def test_class_instance(self):
        example = API_RNA_STRAND.RNA_STRAND('UAAGCCCUA')
        self.assertIsInstance(example, API_RNA_STRAND.RNA_STRAND)

    def test_download_bpseq_structure(self):
        example = API_RNA_STRAND.RNA_STRAND('UAAGCCCUA')
        result = example.download_bpseq_structure()
        expected = "Bpseq file is ready."
        self.assertEqual(result, expected)


class RMSD_calculation(unittest.TestCase):

    def test_rmsd_calculation(self):
        example = API_PROJEKT.rmsd_calculation("5swe_TEST.pdb", "5swe_TEST.pdb")[0]
        expected = 'Normal RMSD: 0.0\nKabsch RMSD: 6.40072443532e-15\nQuater RMSD: 2.48372284113e-17\n'
        self.assertEqual(example, expected)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
