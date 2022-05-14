# Please note, one of these functions' code was inspired from another source.

import string
import english_words

class encryption():
    def __init__(self):
        self.shift = input('Enter the shift: ')
        self.text = list(input('Enter the text you wish to cypher: '))
        newsentence = []

        for i in self.text:
            newlet = chr(ord(i) + int(self.shift))
            newsentence.append(newlet)

        print("".join(newsentence))

        b = input("Do you want to decypher something? (y if yes): ")
        if b == "y":
            self.decypher()
        else:
            print("Closing function")
            return

def sceaser(): # This method and the one above are other methods to do ceasar cipher, although they don't necessarily match the "ideal" method, as shown below
    plaintext = input("Enter plaintext: ")
    shift = int(input("Enter the shift: "))
    shift %= 26
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encrypt = plaintext.translate(table)
    print(encrypt)
    return

def ceasar(text, s, alphabets, punct): 
    def shift(alphabet):
        return alphabet[s:] + alphabet[:s]

    shifted = tuple(map(shift, alphabets))

    fa = ' '.join(alphabets)+" "+punct
    fsa = ' '.join(shifted) +" "+punct

    translation = str.maketrans(fa, fsa)

    return text.translate(translation)

def decode(text, s, alphabets, punct):
    def shift(alphabet):
        return alphabet[s:] + alphabet[:s]

    shifted = tuple(map(shift, alphabets))

    fa = ' '.join(alphabets)+" "+punct
    fsa = ' '.join(shifted) +" "+punct

    table = str.maketrans(fsa, fa)

    return text.translate(table)

def dws():
	d = False
	x = 0
	xy = ""
	decoded = input("Enter plaintext to decode: ")

	while x <= 26:

		xy = decode(decoded,x, [string.ascii_lowercase, string.ascii_uppercase], string.punctuation)
		xyz = xy

		for i in string.punctuation:
			xyz = xyz.replace(i, "")
		
		xyz = xyz.split(" ")

		if xyz[0].lower() in english_words.english_words_set:
			d = True
			print(xy)
			break

		x += 1

	if d == False:
		x = 0
		while x <= 26: 
			xy = decode(decoded, x, [string.ascii_lowercase, string.ascii_uppercase], string.punctuation)
			print(xy, "[shift:", str(x)+"]")
			x += 1

def choose():
	x = input("Encode, decode (with a shift) or decode (without a shift) (a/b/c): ")
	match x:
		case "a":
			print(ceasar(input("Enter plaintext: "), (int(input("Enter shift: ")) % 26), [string.ascii_lowercase, string.ascii_uppercase],  string.punctuation))
		case "b":
			print(decode(input("Enter plaintext: "), (int(input("Enter shift: ")) % 26), [string.ascii_lowercase, string.ascii_uppercase],  string.punctuation))
		case "c":
			dws()

choose()

input()
