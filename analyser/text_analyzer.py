import os
import unittest
import analyser.AnalyseText


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ''analyse_text()'' function."""
    # why cant i do this

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('I gazed upon the cloudless moon\n'
                    'and loved her all the night;\n'
                    'Till morning came, then ardent noon\n'
                    'and I forgot her light.\n')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyser.AnalyseText.AnalyseText.analyse_text(self.filename)

    def test_line_count(self):
        """Check that line count is correct."""
        self.assertEquals(analyser.AnalyseText.AnalyseText.analyse_text(self.filename)[0], 3)

    def test_character_count(self):
        """Check that character count is correct."""
        self.assertEquals(analyser.AnalyseText.AnalyseText.analyse_text(self.filename)[1], 121)

    def test_no_such_file(self):
        """Check correct exception thrown for missing file."""
        with self.assertRaises(IOError):
            analyser.AnalyseText.AnalyseText.analyse_text('foo')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyser.AnalyseText.AnalyseText.analyse_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()
