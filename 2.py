#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description = 'Simply program , reverse  text')
parser.add_argument('-n', help='file name', type=str)
parser.add_argument('-l', help = 'line number', type=int)
parser.add_argument('-v', help = 'file version', type=str)
args = parser.parse_args()

#print(args.n)                                                                                                                                                                              
lines = []


try:
    f = open(args.n)
    lines = f.readlines()
except IOError:
    print ("Error: File does not appear to exist.")
for line in reversed(lines[0:args.l]):
    print(line[::-1])

