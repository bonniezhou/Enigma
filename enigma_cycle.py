#an unused function created while implementing the Enigma machine

cyclic_shift = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]

#0 <= alpha_num <= 25
def cycle(alpha_num):
	cyc = cyclic_shift
	for i in range(alpha_num):
		index = 0
		new_perm = []
		while index < len(cyc):
			new_perm.append(cyc[index]) #optimize to exclude .append
			index += 1
		new_perm.append(cyclic_shift[0])
		cyc = perm_multiply(new_perm)
	return cyc
