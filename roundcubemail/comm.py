#!/usr/bin/python

import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

fp1 = open(f1, 'r')
fl1 = fp1.readlines()
fp1.close()

fp2 = open(f2, 'r')
fl2 = fp2.readlines()
fp2.close()

print "".join([x for x in fl2 if not x in fl1])
