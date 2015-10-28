# A python implementation of the CAT Tool used in Linux
# This can be massively improved+

import sys
from optparse import OptionParser

DEVMODE = True
# DEVMODE is a toggable constant variable, enable to turn on logging etc

if DEVMODE == True:
	import logging
	# imports the loggign module, creates a logging file called "ProgramLog.txt"
	logging.basicConfig(filename='_ProgramLog.txt', level=logging.DEBUG,
						format=' %(asctime)s - %(levelname)s- %(message)s')

class CatCommand:
    logging.debug("at class cat command")
    def __init__(self):
        self.count = 1
        logging.debug("self.count set up")

    def run(self, i, options):
        e = ""
        logging.debug("running")
        print(i)
        for line in i:
            if options.showend:
                line = line.rstrip()
                logging.debug("show end")
            if options.shownum:
                logging.debug("show num")
                line = ("{0} {1}".format(self.count, line))
                e = "$\n"
            logging.debug("looping")
            self.count += 1
            print(line, end=e)
        logging.debug("completed for loop")

def main():
    usage = "usage: %prog [OPTION]... [FILE]..."
    logging.debug("useage set up")
    parser = OptionParser(usage=usage)
    logging.debug("parser set up")
    parser.add_option("-E", dest="showend", action="store_true", help="show $ at line endings")
    logging.debug("show end set up")
    parser.add_option("-n", dest="shownum", action="store_true", help="show line numbers")
    logging.debug("show num set up")
    (options, args) = parser.parse_args()
    logging.debug(options)
    logging.debug("options set up")


    c = CatCommand()
    logging.debug("created class")
    if len(args) > 1:
        logging.debug("called from terminal")
        for a in args:
            f = open(a, 'r')
            c.run(f, options)
            logging.debug("in for loop")
    else:
        logging.debug("else statement")
        logging.debug(options)
        logging.debug(sys.stdin)
        c.run(sys.stdin, options)

if __name__ == "__main__":
    main()
