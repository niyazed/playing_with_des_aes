import pyaes,sys

iv = "InitializationVe"

def key():
	f = open("key-aes.txt" , "r")
	key = f.read()
	f.close()
	if len(key) == 16 or len(key) == 24 or len(key) == 32:
		print("Key: %r" % key)
		print("+-----------------------------+")
		return key
	
	else:
		print("Key has to be  16/24/32 bytes\n")
		default_key = "This_key_for_demo_purposes_only!"
		print ("Using The Default Key: %r" % default_key)
		print("+-----------------------------+")
		return default_key
	
	

def encrypt():
	f = open("input-aes.txt", "r")
	plain = f.read()
	f.close()
	print("+-----------------------------+")
	print("Plaintext: %r" % plain)
	print("+-----------------------------+")
	
	#Encryption
	aes = pyaes.AESModeOfOperationCBC(key(), iv = iv)
	ciphered = aes.encrypt(plain)
	f = open("cipher-aes.txt", "w")
	f.write(str(ciphered))
	f.close()
	print repr("Ciphered: %r" % ciphered)
	print("+-----------------------------+")
	
	
def decrypt():
	f = open("cipher-aes.txt", "r")
	cipher = f.read()
	f.close()
	print("+-----------------------------+")
	print("Ciphertext: %r" % cipher)
	print("+-----------------------------+")
	
	#Decryption
	aes = pyaes.AESModeOfOperationCBC(key(), iv = iv)
	plained = aes.decrypt(cipher)
	print "Deciphered: ", plained
	print("+-----------------------------+")
	
	f = open("plain-aes.txt", "w")
	f.write(str(plained))
	f.close()
	
if len(sys.argv) != 2:
	print("+-----------------------------+")
	print("| Encryption: CipherAES.py 'e'|\n| Decryption: CipherAES.py 'd'|")
	print("+-----------------------------+")
	exit()
	
else:
	if sys.argv[1] == "e":
		encrypt()
		
	elif sys.argv[1] == "d":
		decrypt()
		
	else:
		print("+-----------------------------+")
		print("| Encryption: CipherAES.py 'e'|\n| Decryption: CipherAES.py 'd'|")
		print("+-----------------------------+")
		exit()