def cesarEncoder(decryptedString,key):
	decryptedString = decryptedString.upper().replace(" ","")
	decryptStrLength = len(decryptedString)
	## CHAR -> ASCII
	asciiDecryptedString = [ord(x) for x in decryptedString]
	## Keep only letters
	for i in range(0,decryptStrLength): asciiDecryptedString[i] = (asciiDecryptedString[i]-65)%26
	## Ciphering
	asciiEncryptedString = [((asciiDecryptedString[i]+key)%26) for i in range(0,decryptStrLength)]
	## Stop keep only letters
	for i in range(0,decryptStrLength): asciiEncryptedString[i] = (asciiEncryptedString[i]+65)
	## ASCII -> CHAR
	encryptedString = [chr(y) for y in asciiEncryptedString]
	return "".join(encryptedString)