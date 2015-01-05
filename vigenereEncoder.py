def vigenereEncoder(decryptedString,key):
	decryptedString = decryptedString.upper()
	decryptStrLength = len(decryptedString)
	## Repeat the key as many times as necessary
	key = [key[i%len(key)] for i in range(0,decryptStrLength)]
	## CHAR -> ASCII
	asciiKey = [ord(x) for x in key]
	asciiDecryptedString = [ord(x) for x in decryptedString]
	## Keep only letters
	for i in range(0,decryptStrLength):
		asciiKey[i] = (asciiKey[i]-65)%26
		asciiDecryptedString[i] = (asciiDecryptedString[i]-65)%26
	## Ciphering
	asciiEncryptedString = [((asciiDecryptedString[i]+asciiKey[i])%26) for i in range(0,decryptStrLength)]
	## Stop keep only letters
	for i in range(0,decryptStrLength):
		asciiEncryptedString[i] = (asciiEncryptedString[i]+65)
	## ASCII -> CHAR
	encryptedString = [chr(y) for y in asciiEncryptedString]
	return "".join(encryptedString)