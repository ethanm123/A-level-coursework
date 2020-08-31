class Caesar:
    """Class containing the code for the Caesar cipher"""
    def __init__(self, plain_text=None, shift=None):
        self.plain_text=plain_text
        self.shift=shift

    def decrypt(self, plain_text, shift=""):
        """If decrypting it makes a call to the normal Caesar function but specifying that a decryption is occuring"""
        return self.caesar(self, plain_text, shift, True)

    def caesar(self, plain_text, shift, decrypt=False):
        """Carries out the Caesar cipher algorithm and returns the result."""
        if plain_text == "":
            return("You might want to enter a message.")
        self.plain_text = plain_text.lower()
        self.shift = int(shift)
        alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                             "u", "v", "w", "x", "y", "z"]

        encrypted_string = ""
        if self.shift > 26:
            while self.shift > 26:
                self.shift -= 26

        if decrypt == True:
            self.shift = 26-self.shift

        for i in self.plain_text:
            if i in alphabet_list:
                amount = alphabet_list.index(i) + self.shift
                if amount >= 26:
                    amount -= 26
                encrypted_string += alphabet_list[amount]
            else:
                encrypted_string += i
        return encrypted_string




