from implementation_PageRank import *

distrib = iter(0.85, [10**-6], FILE)

print(sum(distrib[0][2]))