#from speck import SpeckCipher
from Crypto.Cipher import AES
class Security:

    def __init__(self,bit,mode):
        self.bit = bit
        self.key = bytes('abcdefghijklmnop',encoding='utf-8')
        self.mode = mode
        print(self.mode)
    
    def padding(self,originalPayload):
        
        paddedPayload = originalPayload+"\0" *(AES.block_size-len(originalPayload)%AES.block_size)
        print(paddedPayload)
        return paddedPayload

    def speckEncryptor(self):
        pass

    def speckDecryptor(self):
        pass

    def aesEncryptor(self,payload):
        try:
            print("Called!!")
            from Crypto.Cipher import AES
            if not self.mode:
                self.mode = AES.MODE_ECB
            cipher = AES.new(self.key, AES.MODE_ECB)
            payload = self.padding(payload)
            encryptedPayload = cipher.encrypt(payload)
            print("Encrypted Data>>",encryptedPayload)
            return encryptedPayload
        except Exception as e:
            print(e)

    def aesDecryptor(self,encryptedPayload):
    
        from Crypto.Cipher import AES
        if not self.mode:
            self.mode = AES.MODE_ECB
        cipher = AES.new(self.key,AES.MODE_ECB)
        originalPayload = cipher.decrypt(encryptedPayload)
        try:
            #cipher.verify(tag)
            print("The message is authentic:", originalPayload)
            return originalPayload
        except ValueError:
           print("Key incorrect or message corrupted")