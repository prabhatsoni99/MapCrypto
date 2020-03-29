"""
In randint(start,end), includes the final value(end)
We are using 0-99

100! is approx number of possible combinations which
is 10^24 which is v large so chill scene
"""

from random import randint

N = randint(80,100) #100 is included. if N=100 no prob

left_nodes = [i for i in range(100)]
sequence = []

for i in range(N):
	ok_pos = randint(0,len(left_nodes)-1) #includes end value so we have to do -1
	#print(ok_pos, left_nodes[ok_pos])
	sequence.append(left_nodes[ok_pos])
	left_nodes.pop(ok_pos)

sequence_str = str(sequence)[1:-1]
sequence_str = sequence_str.replace(", " , " ")
print(sequence_str)
