
import pathlib

# Checking a file for a suffix
def check_suffix(filename, suffix=".ini"):
    return (True if pathlib.Path(filename).suffix == suffix else False)

# Checking the file for existence by the specified path
def check_file(filename):
    return pathlib.Path(filename).is_file()

