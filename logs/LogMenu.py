import argparse
from logs import LogLoader

class LogMenu:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--csv', help='File path for CSV file')
        self.parser.add_argument('--xes', help='File path for XES file')
        self.parser.add_argument('--ocel', help='File path for OCEL file')

    def run(self):
        args = self.parser.parse_args()
        if sum(map(bool, [args.csv, args.xes, args.ocel])) != 1:
            raise Exception("Please provide exactly one argument")
        elif args.csv:
            return LogLoader.load_csv(args.csv)
        elif args.xes:
            return LogLoader.load_xes(args.xes)
        elif args.ocel:
            return LogLoader.load_ocel(args.ocel)
        else:
            raise Exception("Please provide an argument --xes, --csv or --ocel")

