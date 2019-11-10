from speck import SpeckCipher

class Security:

    def __init__(self,bit,mode=None):
        self.bit = bit
        self.key = "something"
        self.mode = mode
    
    def speckEncryptor(self):
        pass

    def speckDecryptor(self):
        pass

    def aesEncryptor(self,payload):
        from Crypto.Cipher import AES
        if not self.mode:
            self.mode = AES.MODE_EAX
        cipher = AES.new(self.key, self.mode)
        nonce = cipher.nonce
        encryptedPayload, tag = cipher.encrypt_and_digest(payload)
        return encryptedPayload

    def aesDecryptor(self,encryptedPayload):
        from Crypto.Cipher import AES
        if not self.mode:
            self.mode = AES.MODE_EAX
        cipher = AES.new(self.key, self.mode, nonce=nonce)
        originalPayload = cipher.decrypt(encryptedPayload)
        try:
            cipher.verify(tag)
            print("The message is authentic:", originalPayload)
            return originalPayload
        except ValueError:
           print("Key incorrect or message corrupted")