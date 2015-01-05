def vigenereDecoder(encryptedString,key):
	encryptedString = encryptedString.upper()
	encryptStrLength = len(encryptedString)
	## Repeat the key as many times as necessary
	key = [key[i%len(key)] for i in range(0,encryptStrLength)]
	## CHAR -> ASCII
	asciiKey = [ord(x) for x in key]
	asciiEncryptedString = [ord(x) for x in encryptedString]
	## Keep only letters
	for i in range(0,encryptStrLength):
		asciiKey[i] = (asciiKey[i]-65)%26
		asciiEncryptedString[i] = (asciiEncryptedString[i]-65)%26
	## Decipherment
	asciiDecryptedString = [((asciiEncryptedString[i]-asciiKey[i])%26) for i in range(0,encryptStrLength)]
	## Stop keep only letters
	for i in range(0,encryptStrLength):
		asciiDecryptedString[i] = (asciiDecryptedString[i]+65)
	## ASCII -> CHAR
	decryptedString = [chr(y) for y in asciiDecryptedString]
	return "".join(decryptedString)