import ElementPool, sys

if (len(sys.argv) == 1):
   print "USAGE: {0} <pool text file>".format(sys.argv[0])
   exit(1)

file = sys.argv[1]
pool = ElementPool.ElementPool(file)

print pool
exit(0)
