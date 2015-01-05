def cesarDecoder(encryptedString,key):
	encryptedString = encryptedString.upper()
	encryptStrLength = len(encryptedString)
	## CHAR -> ASCII
	asciiEncryptedString = [ord(x) for x in encryptedString]
	## Keep only letters
	for i in range(0,encryptStrLength): asciiEncryptedString[i] = (asciiEncryptedString[i]-65)%26
	## Decipherment
	asciiDecryptedString = [((asciiEncryptedString[i]-key)%26) for i in range(0,encryptStrLength)]
	## Stop keep only letters
	for i in range(0,encryptStrLength): asciiDecryptedString[i] = (asciiDecryptedString[i]+65)
	## ASCII -> CHAR
	decryptedString = [chr(y) for y in asciiDecryptedString]
	return "".join(decryptedString)