import sys
import argparse

from grader import Grader

def main(path, details, verbose):
    try:
        grader = Grader()
        grader.run(path, details, verbose)

    except Exception as e:
        print("Exception occured:", e, traceback.format_exc())
        print(e)
        sys.exit()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Readability Calculator')
    parser.add_argument('--details', '-d', action='store_true', help='Display calculation details')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('path',   type=str, help='Name of the test cases directory')

    args = parser.parse_args()
    main(args.path, args.details, args.verbose)
