from math import sqrt

"""
computes dist(a1,a2) + dist(a2,a3) + .... + dist(an-1, an)
"""


def make_map_arr():
	obj = open("map.txt")

	maparr = []
	for i in obj:
		maparr.append(str(i))

	for i in range(len(maparr)):
		maparr[i] = maparr[i][:-1].split()
		maparr[i][0] = int(maparr[i][0])
		maparr[i][1] = float(maparr[i][1])
		maparr[i][2] = float(maparr[i][2])

	return maparr



def get_input():
	sequence = list(map( int, input().split() ))
	return sequence



def dist(x1,y1,x2,y2):
	distance = sqrt( (x1-x2)**2 + (y1-y2)**2 )
	return distance


def compute_sequence_total(sequence, maparr):
	"""This is not circular atm
	"""
	total = 0
	#print(maparr)
	for i in range(len(sequence)-1): #i,i+1 so we cannot do i+1 of last coordinate
		x1 = maparr[ sequence[i] ][1]
		y1 = maparr[ sequence[i] ][2]
		x2 = maparr[ sequence[i+1] ][1]
		y2 = maparr[ sequence[i+1] ][2]
		total += dist(x1,y1,x2,y2)
	return total


def input_is_safe(sequence, maparr):
	"""
		- Must only allow if atleast 80% of coordinates, otherwise reject
		- All nodes must be unique
		Otherwise attacker can leak info about the nodes
	"""
	if len(sequence) < 0.8*len(maparr):
		return False
	unique_checker = []
	for i in sequence:
		if i in unique_checker:
			return False
		unique_checker.append(i)
	return True


if __name__=="__main__":
	sequence = get_input()
	maparr = make_map_arr()
	if input_is_safe(sequence, maparr):
		total = compute_sequence_total(sequence,maparr)
		print(total)
	else:
		print("ERROR: THE INPUT IS UNSAFE")

