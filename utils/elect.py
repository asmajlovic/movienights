#!/usr/bin/python
import random
import sys
from collections import Counter

candidates = ['Adnan', 'Andrew', 'Daniele', 'Marius', 'Sushil', 'Matteo', 'Duncan']

def help():
    print """Usage: elect.py <former president #1> <former president #2>

Available candidates: {0}""".format(", ".join(candidates))

try:
    candidates.remove(sys.argv[1])
    candidates.remove(sys.argv[2])
except ValueError:
    print "The two former incarnation of El Presidente must be valid candidates\n"
    help()
    sys.exit(1)
except IndexError:
    print "Please specify the two last incarnations of El Presidente\n"
    help()
    sys.exit(1)


results = Counter()
for vote in xrange(1000000):
   random.shuffle(candidates)
   results.update([candidates[0]])

d = dict(results.items())
el_presidente = sorted(d, key=d.get)[-1]
print "The new El Presidente is {0}. Congratulations!".format(el_presidente)
