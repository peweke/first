class AnalyseText():

    def analyse_text(filename):
        """Calculate the number of lines and characters in a file

        Args:
            filename: The name of the file to analyse.

        Raises:
            IOError: If ''filename'' does not exist or can't be read.

        Returns: A tuple where the first element is the number of lines in the file
            and the second element is the number of characters.
        """
        lines = 0
        chars = 0
        with open(filename, 'r') as f:
            for line in f:
                lines += 1
                chars += len(line)
            return lines, chars