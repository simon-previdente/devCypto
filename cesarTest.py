# -*-coding:Utf-8 -*
import unittest
from cesarEncoder import *
from cesarDecoder import *

class cesarTest(unittest.TestCase):
	def testCesarEncoderWithZeroKey(self):
		myString = "CESAR"
		self.assertEqual(cesarEncoder(myString,0), myString)
	def testCesarEncoder(self):
		myPangram = "Monsieur Jack vous dactylographiez bien mieux que votre ami Wolf"
		myKey = 42
		self.assertEqual(cesarEncoder(myPangram,myKey), "CEDIYUKHZQSALEKITQSJOBEWHQFXYUPRYUDCYUKNGKULEJHUQCYMEBV")
	
	def testCesarDecoderWithZeroKey(self):
		myString = "CESAR"
		self.assertEqual(cesarDecoder(myString,0), myString)
	def testCesarDecoder(self):
		encipheredMessage = "DfejzvliArtbmfljurtkpcfxirgyzvqszvedzvlohlvmfkivrdzNfcw"
		myKey = 69
		self.assertEqual(cesarDecoder(encipheredMessage,myKey), "MONSIEURJACKVOUSDACTYLOGRAPHIEZBIENMIEUXQUEVOTREAMIWOLF")
	
	def testICanDecryptAMessageThatIHaveEncrypted(self):
		myString = "GOODJOB"
		myKey = 255
		encipheredMessage = cesarEncoder(myString,myKey)
		self.assertEqual(cesarDecoder(encipheredMessage,myKey), myString)


if __name__ == '__main__':
    unittest.main()