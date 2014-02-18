#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random
from collections import Counter

def main():
    """
    Run through a string list of candidates and pseudo-randomly increase
    the relevant vote count.  Highest count for any given list element
    is the elected candidate
    """
    parser = argparse.ArgumentParser(description="Elect a new movie night "
                                                    "president")
    parser.add_argument("-t", "--votes", action="store", required=False,
                        metavar="VOTES_AVAILABLE", type=int,
                        help="Total number of votes to cast",
                        default=1000000)
    parser.add_argument("-c", "--candidates", action="store", required=True,
                        metavar="CANDIDATE_LIST", nargs="+", type=str,
                        help="List of candidates to be considered")

    # Parse arguments (validate user input)
    args = parser.parse_args()

    results = Counter()
    for vote in xrange(args.votes):
        random.shuffle(args.candidates)
        results.update([args.candidates[0]])

    d = dict(results.items())
    el_presidente = sorted(d, key=d.get)[-1]
    print "The new El Presidente is {0}. Congratulations!".format(el_presidente)


# Run the damn thing...
if __name__ == '__main__':
    main()    

