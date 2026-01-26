import sys
import time
import logging
import traceback
import threading

from datetime import datetime

from loader import Loader
from runner import Runner

class Grader():
    def run(self, path, details, verbose):
        """Run"""
        loader = Loader(path)
        runner = Runner()

        def prompt():
            print("h     - Print this message.")
            print("s     - Scan for sources.")
            print("l     - List available sources.")
            print("#|all - Run n-th source or all.")
            print("q     - Quit.")

        while True:
            try:
                opt = str(input("==> ")).strip()
            except Exception as e:
                break

            if not opt:
                continue
            if  opt == 'h' or opt == '?':
                prompt()
                continue
            if  opt == 's':
                loader.scan()
                print("Loaded {} sources".format(loader.size()))
                continue
            if  opt == 'l':
                loader.list()
                continue
            if  opt == 'q':
                break
            if  opt == 'all':
                for idx in range(1, loader.size() + 1):
                    runner.run(loader.file(idx), details, verbose)
                continue
            else:
                try:
                    idx = int(opt)
                    if idx > 0 and idx <= loader.size():
                        runner.run(loader.file(idx), details, verbose)
                        continue
                except Exception as e:
                    print("Exception occured:", e, traceback.format_exc())
                    continue

                print("Invalid option:", opt)

