import os
import sys

class Record:
    def __init__(self, path):
        self.path = path

class Loader:
    def __init__(self, path):
        sys.path.insert(1, path)
        self.path  = path
        self.files = []
        self.scan()

    def scan(self):
        self.files.clear()
        for root, subdirs, files in os.walk(self.path):
            for filename in files:
                if filename.endswith(".txt"):
                    path = os.path.join(root, filename)
                    self.files.append(Record(path))
        self.files.sort(key = lambda r: (r.path))

    def list(self):
        for i in range(0, len(self.files)):
            r = self.files[i]
            print('%3d - %s' % (i + 1, r.path))

    def file(self, idx):
        return self.files[idx - 1].path

    def size(self):
        return len(self.files)

