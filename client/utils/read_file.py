def read_file(filename):
    """
    Reads a file and returns the contents.

    Parameters
    ----------
    filename : str
        The name of the file to read.
    """

    with open(filename, 'r') as f:
        return f.read()
