def read_file(filename):
    """
    Reads a file and returns the contents.
    """
    with open(filename, 'r') as f:
        return f.read()
