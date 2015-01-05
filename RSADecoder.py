def RSADecoder(chiffre, premier_composant, deuxieme_composant) :
	
	def power(value, puiss, modulo):
		result = value
		for num in range(1,puiss):
			result = result*value%modulo
		return result


	message_chiffre = [power(num, deuxieme_composant, premier_composant) for num in chiffre]
	message_clair = [chr(char%256) for char in message_chiffre]
		
	
	return "".join(message_clair)
