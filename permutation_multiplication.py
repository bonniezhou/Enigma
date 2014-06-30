#Permutation Multiplication
#--------------------------------------------

#collapse: (listof (listof int)) -> (listof int)
#collapses a two-level nested list into a flat list
def collapse(alist):
    newlist = []
    for a in alist:
        for b in a:
            if b not in newlist:
                newlist.append(b)
    return newlist


#perm_next: int (listof int) -> int
#returns the mapping of a in perm
#a must be in perm
#perm has no duplicates
def perm_next(a, perm):
    for i in range(0, len(perm)):
        if a == perm[i]:
            if i == len(perm) - 1:
                return perm[0]
            else:
                return perm[i+1]

#----------------------------------------------

#perm_map: int (listof (listof int)) -> int
#returns the mapping of a in a product of permutations list_of_perms
#Example: perm_map(7, [[1,2,3,7,4],[6,3,7,4],[6,3,5]]) => 1
def perm_map(a, list_of_perms):
    if len(list_of_perms) == 0:
        return a
    last_perm = list_of_perms[len(list_of_perms)-1]
    if a in last_perm:
        return perm_map(perm_next(a, last_perm), list_of_perms[:len(list_of_perms)-1])
    else:
        return perm_map(a, list_of_perms[:len(list_of_perms)-1])


#perm_multiply: (listof (listof int)) -> (listof (listof int))
#returns the simplified product of permutations in list_of_perms
#Example: perm_multiply([[1,2,3,7,4],[6,3,7,4],[6,3,5]]) => [[1,2,3,5,7],[4,6]]
def perm_multiply(list_of_perms):
    perm_elements = collapse(list_of_perms)
    perm = []
    range_elements = range(min(perm_elements), max(perm_elements) + 1)
    single_perm = []
    i = 1
    while len(range_elements) != 0:
        single_perm.append(i)
        range_elements.remove(i)
        i = perm_map(i, list_of_perms)
        if i == single_perm[0]:
            if len(single_perm) > 1:
                perm.append(single_perm)
            single_perm = []
            if len(range_elements) != 0:
                i = range_elements[0]
            else:
                return perm

#---------------------------------------------

#perm_inverse_next: int (listof int) -> int
#returns the inverse mapping of a in perm
#a must be in perm, and perm must have no duplicates
def perm_inverse_next(a, perm):
    for i in range(0, len(perm)):
        if a == perm[i]:
            if i == 0:
                return perm[len(perm) - 1]
            else:
                return perm[i-1]


#perm_inverse_map: int (listof (listof int)) -> int
#returns the inverse mapping of a in a product of DISJOINT permutations list_of_perms
#Example: perm_inverse_map(7, [[1,2,3,5,7],[4,6]]) => 5
def perm_inverse_map(a, list_of_perms):
	for perm in list_of_perms:
		if a in perm:
			return perm_inverse_next(a, perm)
	else:
		return a
