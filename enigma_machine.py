#Enigma Machine Simulation
#---------------------------------------------
#This simulation includes the choice of all 8 rotors
#from the Enigma I, M3 Army, and M3 and M4 Naval.
#It also includes reflectors A, B, and C as used
#in the war. It encrypts all non-letter entries as
#whitespace.
#---------------------------------------------

from permutation_multiplication import *

#---------------------------------------------
#alpha_map maps char to 0, 1, ...., 25 if it is an
#English letter, and maps it to -1 otherwise
#Pre-cond: char must be a single-character string
def alpha_map(char):
	if 65 <= ord(char) and ord(char) <= 90:
		return ord(char) - 65
	elif 97 <=ord(char) and ord(char) <= 122:
		return ord(char) - 97
	else:
		return -1

#inverse_alpha_map maps integers 0,...,25 to letters
#of the alphabet, and -1 to a black space
#Pre-cond: -1 <= num <= 25
def inverse_alpha_map(num):
	if num == -1:
		return ' '
	else:
		return chr(num+65)

#---------------------------------------------

#encrypt maps char to its corresponding encryption on the Enigma machine
#encrypt produces an int in [0,...,25]
#Pre-conds:
#	char, keys[0], keys[1], keys[2] are all integers in [0,...,25]
#	keys is a 3-element list
#	rot1, rot2, rot3, ref are each a product of disjoint cycles
#	rot1 refers to the outermost rotor and rot3 is the innermost rotor
def encrypt(char, keys, rot1, rot2, rot3, ref):
	if char < 0 or char > 25:
		return char
	sequence = [keys[0], rot1, keys[1], rot2, keys[2], rot3, 0]
	prev_key = 0
	for mapping in sequence:
		if type(mapping) is int:
			char = (char + (mapping-prev_key)) % 26
			prev_key = mapping
		else:
			char = perm_map(char, mapping)

	char = perm_map(char, ref)
	
	i = len(sequence) - 1
	while i >= 0:
		if type(sequence[i]) is int:
			if i > 1:
				char = (char - (sequence[i]-sequence[i-2])) % 26
			else:
				char = (char - sequence[i]) % 26
		else:
			char = perm_inverse_map(char, sequence[i])
		i -= 1
	
	return char

#str_to_perm converts the string alpha to its corresponding permutation
#Pre-cond: alpha is a string of the 26 unique English letters of the alphabet
def str_to_perm(alpha):
	new_perm = []
	
	i = 0
	letters_used = []
	mini_perm = []
	while len(letters_used) < 26:
		if len(mini_perm) == 0:
			mini_perm.append(i)
			letters_used.append(i)
			i = alpha_map(alpha[i])
		elif i == mini_perm[0]:
			new_perm.append(mini_perm)
			mini_perm = []
			for letter in range(26):
				if letter not in letters_used:
					i = letter
					break
		else:
			mini_perm.append(i)
			letters_used.append(i)
			i = alpha_map(alpha[i])

	return new_perm

#---------------------------------------------

#Rotors and reflectors used in the Enigma machine

rotor1 = str_to_perm("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotor2 = str_to_perm("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotor3 = str_to_perm("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotor4 = str_to_perm("ESOVPZJAYQUIRHXLNFTGKDCMWB")
rotor5 = str_to_perm("VZBRGITYUPSDNHLXAWMJQOFECK")
rotor6 = str_to_perm("JPGVOUMFYQBENHZRDKASXLICTW")
rotor7 = str_to_perm("NZJHGRCXMYSWBOUFAIVLPEKQDT")
rotor8 = str_to_perm("FKQHTLXOCBJSPDZRAMEWNIUYGV")
reflectorA = str_to_perm("EJMZALYXVBWFCRQUONTSPIKHGD")
reflectorB = str_to_perm("YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflectorC = str_to_perm("FVPJIAOYEDRZXWGCTKUQSBNMHL")

rotors = [rotor1, rotor2, rotor3, rotor4, rotor5, rotor6, rotor7, rotor8]
reflectors = [reflectorA, reflectorB, reflectorC]

#---------------------------------------------

#enigma asks the user to select the 3 rotors, 3 message keys, and the
#reflector to be used, then prints out the encryption of the input message
def enigma():
	
	#select rotors
	while True:
		try:
			rot1 = int(raw_input("Choose a rotor (1 to 8): "))
			if 1 <= rot1 <= 8:
				break
			else:
				print("Number not in range.")
		except ValueError:
			print("Invalid")
	while True:
		try:
			rot2 = int(raw_input("Choose a 2nd rotor (1 to 8, not " + str(rot1) + "): "))
			if 1 <= rot1 <= 8 and rot2 != rot1:
				break
			else:
				print("Number not in range.")
		except ValueError:
			print("Invalid")
	while True:
		try:
			rot3 = int(raw_input("Choose a 3rd rotor (1 to 8, not " + str(rot1) + " or " + str(rot2) + "): "))
			if 1 <= rot1 <= 8 and rot3 != rot1 and rot3 != rot2:
				break
			else:
				print("Number not in range.")
		except ValueError:
			print("Invalid")
	
	rot1 = rotors[rot1 - 1]
	rot2 = rotors[rot2 - 1]
	rot3 = rotors[rot3 - 1]

	#select keys
	while True:
		try:
			key1 = alpha_map(raw_input("Choose a key between A to Z: "))
			if 0 <= key1 <= 25:
				break
			else:
				print("You did not enter a letter.")
		except TypeError:
			print("Invalid")
	while True:
		try:
			key2 = alpha_map(raw_input("Choose a 2nd key between A to Z: "))
			if 0 <= key2 <= 25:
				break
			else:
				print("You did not enter a letter.")
		except TypeError:
			print("Invalid")
	while True:
		try:
			key3 = alpha_map(raw_input("Choose a 3rd key between A to Z: "))
			if 0 <= key3 <= 25:
				break
			else:
				print("You did not enter a letter.")
		except TypeError:
			print("Invalid")
	
	keys = [key1, key2, key3]

	#select reflector
	while True:
		try:
			ref = alpha_map(raw_input("Choose a reflector (A, B, or C): "))
			if 0 <= ref <= 2:
				ref = reflectors[ref]
				break
			else:
				print("You did not enter A, B, or C")
		except TypeError:
			print("Invalid")

	#encrypt message
	i = 0
	message = raw_input("Type in your secret message: ")
	encryption = ""
	while i < len(message):
		code = encrypt(alpha_map(message[i]), [key1+i, key2+(i/26), key3+(i/676)], rot1, rot2, rot3, ref)
		encryption = encryption + inverse_alpha_map(code)
		i += 1

	print(encryption)


