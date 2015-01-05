def RSAEncoder(message, premier_composant, deuxieme_composant):
	
	def power(value, puiss, modulo):
		result = value
		for num in range(1,puiss):
			result = result*value%modulo
		return result
	
	message_ascii = [ord(char) for char in message]
	secret_chiffre =  [power(num, deuxieme_composant, premier_composant) for num in message_ascii]
	
	return [chiffre for chiffre in secret_chiffre]