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
            print("h           - Print this message.")
            print("s           - Scan for sources.")
            print("l           - List available sources.")
            print("#|all [xyz] - Run n-th source or all sources.")
            print("              An optional argument can be used to only run a single readability formula:")
            for code, description in runner.formulas():
                print("{:>20} - {:}".format(code, description))
            print("q           - Quit.")






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
            else:
                try:
                    opts = opt.split(' ')
                    if opts[0] == 'all':
                        for idx in range(1, loader.size() + 1):
                            runner.run(loader.file(idx), '*', details, verbose)
                    else:
                        idx = int(opts[0])
                        if idx > 0 and idx <= loader.size():
                            if len(opts) > 1:
                                runner.run(loader.file(idx), opts[1], details, verbose)
                            else:
                                runner.run(loader.file(idx), '*', details, verbose)
                    continue
                except Exception as e:
                    print("Exception occured:", e, traceback.format_exc())
                    continue

                print("Invalid option:", opt)

