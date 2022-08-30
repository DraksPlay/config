
def check_suffix(filename, suffix=".ini"):
    import pathlib
    return (True if pathlib.Path(filename).suffix == suffix else False)

def check_file(filename):
    pass

