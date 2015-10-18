"""
Command line program that shows information about different file types in a specified folder.
"""
# !/user/bin/python3

from collections import defaultdict
from pathlib import Path
import sys

def fetchFileInfo():
    return {
        "fileSize":0,
        "count":0,
    }

def main():
    global files
    if len(sys.argv) != 2:
        print
        ("usage: ext_info.py path\n"
         "displays number of files and total size of files per extension in the specified path.")
    # Traverse the files in the folder
    folder = Path(sys.argv[1])
    files = defaultdict(fetchFileInfo)
    for p in folder.iterdir():
        if p.is_file():
            suffixKey = p.suffix[1:]
            if not suffixKey:
                suffixKey = "."
            files[suffixKey]["fileSize"] += p.stat().st_size
            files[suffixKey]["count"] += 1
    for name, info in sorted(files.items()):
        print ( "%s %d %d"%(name, info["count"],info["fileSize"]) )
        print
if __name__ == "__main__":
    main()
