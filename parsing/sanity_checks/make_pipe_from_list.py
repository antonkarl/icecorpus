#This uses utf-8
#file takes a list of things with each thing on a line and outputs a list separated by pipe

import sys,string

list = sys.stdin.read().split()

ii = 1
sys.stdout.write(list[0])

while ii <= (len(list)-1):
    sys.stdout.write("|%s" % list[ii])
    ii = ii+1
