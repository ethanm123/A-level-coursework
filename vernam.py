class Vernam:
    """Class containing the code of the Vernam cipher"""
    def __init__(self, message=None, key=None):
        self.message = message
        self.key = key

    def vernam(self, message="", key="", ciphertext_to=""):
        """Carries out the Vernam cipher for encryption and decryption. If message has characters then encryption
        is occuring, if ciphertext_to has characters then decryption is occuring. It then carries out the cipher
        on whichever string needs operating on and then returns the result."""
        if message != "":
            self.message = [ord(i) for i in message]
        elif ciphertext_to!="":
            ciphertext_to += " "
            working_message = []
            temp=""
            for i in ciphertext_to:
                if i == " ":
                    working_message.append(int(temp))
                    temp = ""
                else:
                    try:
                        int(i)
                        temp += str(i)
                    except:
                        pass
            self.message = working_message
        self.key = key
        self.key = [ord(i) for i in self.key]
        print(self.message)
        try:
            if len(self.key) < len(self.message):
                while len(self.key)< len(self.message):
                    i=0
                    self.key.append(self.key[i])
                    if i +1 > len(self.key):
                        i=0
                    else: i+=1
            elif len(self.key) > len(self.message):
                self.key = self.key[:len(self.message)]
            ciphertext=""
        except: return "Please enter both a message and a key"
        for i in range(0, len(self.message)):
            if ciphertext_to == "":
                ciphertext+= (str(self.message[i] ^ self.key[i])+" ")
            elif ciphertext_to != "":
                ciphertext+= (str(chr(self.message[i] ^ self.key[i])))
        return ciphertext

