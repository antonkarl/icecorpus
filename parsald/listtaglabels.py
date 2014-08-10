# This Python file uses the following encoding: utf-8
# 
#  Lists all tags in a psd file in alphabetical order
#  Usage:  python listtaglabels.py filename.psd
#

import sys,re

text = open(sys.argv[1]).read()

results = re.findall('\(([^\(\)]*) ([^\(\)]*)\)',text)
xx = []
for result in results:
  xx.append(result[0])

xx = sorted(set(xx))
for x in xx:
  print x
