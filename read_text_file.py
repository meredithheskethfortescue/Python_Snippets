def read_text_file(path: str) -> str:
    """Read a complete textfile
    Useful for e.g. *.html or mySQL files
    """
    with open(path, 'r') as f:
        txt = f.read()
    return txt
