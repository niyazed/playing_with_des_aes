import sys
from pyDes import *

	
def key():
	f = open("key-des.txt" , "r")
	key = f.read()
	f.close()
	if len(key) != 8:
		print("Key has to be a multiple of 8 bytes | e.g 12345678")
	print("Key: %r" % key)
	print("+-----------------------------+")
	return key
	

def encrypt():
	f = open("input-des.txt", "r")
	plain = f.read()
	f.close()
	print("+-----------------------------+")
	print("Plaintext: %r" % plain)
	print("+-----------------------------+")
	
	#Encryption
	d = des()
	ciphered = d.encrypt(key(),plain,padding=True)
	f = open("cipher-des.txt", "w")
	f.write(str(ciphered))
	f.close()
	print ("Ciphered: %r" % ciphered)
	print("+-----------------------------+")
	
	
def decrypt():
	f = open("cipher-des.txt", "r")
	cipher = f.read()
	f.close()
	print("+-----------------------------+")
	print("Ciphertext: %r" % cipher)
	print("+-----------------------------+")
	
	#Decryption
	d = des()
	plained = d.decrypt(key(),cipher,padding=True)
	print "Deciphered: ", plained
	print("+-----------------------------+")
	
	f = open("plain-des.txt", "w")
	f.write(str(plained))
	f.close()

	
	
if len(sys.argv) != 2:
	print("+-----------------------------+")
	print("| Encryption: CipherDES.py 'e'|\n| Decryption: CipherDES.py 'd'|")
	print("+-----------------------------+")
	exit()
	
else:
	if sys.argv[1] == "e":
		encrypt()
		
	elif sys.argv[1] == "d":
		decrypt()
		
	else:
		print("+-----------------------------+")
		print("| Encryption: CipherDES.py 'e'|\n| Decryption: CipherDES.py 'd'|")
		print("+-----------------------------+")
		exit()