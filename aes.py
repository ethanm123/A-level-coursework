def convert_message(message):
    """Converts text into a matrix format in order to be processed by the cipher"""
    converted_message = [hex(ord(i)) for i in message]
    list1 = [converted_message[0], converted_message[1], converted_message[2], converted_message[3]]
    list2 = [converted_message[4], converted_message[5], converted_message[6], converted_message[7]]
    list3 = [converted_message[8], converted_message[9], converted_message[10], converted_message[11]]
    list4 = [converted_message[12], converted_message[13], converted_message[14], converted_message[15]]
    matrix = [list1, list2, list3, list4]
    return matrix

def convert_matrix(matrix):
    """Converts a matrix into a string for outputting decrypted ciphertext"""
    string = ""
    for i in matrix:
        for j in i:
            string += chr(j)
    return string

hex_Values = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]#List of hex values in correct positions

round_constant = [[1,0,0,0], [2,0,0,0], [4,0,0,0], [8,0,0,0], [16,0,0,0], [32,0,0,0], [64,0,0,0], [128,0,0,0], [27,0,0,0], [54,0,0,0]]#Standard Rijndael Round Constant

sub_box = (#Standard Rijndael sbox
    ["0x63", "0x7c", "0x77", "0x7b", "0xf2", "0x6b", "0x6f", "0xc5", "0x30", "0x01", "0x67", "0x2b", "0xfe", "0xd7", "0xab", "0x76"],
    ["0xca", "0x82", "0xc9", "0x7d", "0xfa", "0x59", "0x47", "0xf0", "0xad", "0xd4", "0xa2", "0xaf", "0x9c", "0xa4", "0x72", "0xc0"],
    ["0xb7", "0xfd", "0x93", "0x26", "0x36", "0x3f", "0xf7", "0xcc", "0x34", "0xa5", "0xe5", "0xf1", "0x71", "0xd8", "0x31", "0x15"],
    ["0x04", "0xc7", "0x23", "0xc3", "0x18", "0x96", "0x05", "0x9a", "0x07", "0x12", "0x80", "0xe2", "0xeb", "0x27", "0xb2", "0x75"],
    ["0x09", "0x83", "0x2c", "0x1a", "0x1b", "0x6e", "0x5a", "0xa0", "0x52", "0x3b", "0xd6", "0xb3", "0x29", "0xe3", "0x2f", "0x84"],
    ["0x53", "0xd1", "0x00", "0xed", "0x20", "0xfc", "0xb1", "0x5b", "0x6a", "0xcb", "0xbe", "0x39", "0x4a", "0x4c", "0x58", "0xcf"],
    ["0xd0", "0xef", "0xaa", "0xfb", "0x43", "0x4d", "0x33", "0x85", "0x45", "0xf9", "0x02", "0x7f", "0x50", "0x3c", "0x9f", "0xa8"],
    ["0x51", "0xa3", "0x40", "0x8f", "0x92", "0x9d", "0x38", "0xf5", "0xbc", "0xb6", "0xda", "0x21", "0x10", "0xff", "0xf3", "0xd2"],
    ["0xcd", "0x0c", "0x13", "0xec", "0x5f", "0x97", "0x44", "0x17", "0xc4", "0xa7", "0x7e", "0x3d", "0x64", "0x5d", "0x19", "0x73"],
    ["0x60", "0x81", "0x4f", "0xdc", "0x22", "0x2a", "0x90", "0x88", "0x46", "0xee", "0xb8", "0x14", "0xde", "0x5e", "0x0b", "0xdb"],
    ["0xe0", "0x32", "0x3a", "0x0a", "0x49", "0x06", "0x24", "0x5c", "0xc2", "0xd3", "0xac", "0x62", "0x91", "0x95", "0xe4", "0x79"],
    ["0xe7", "0xc8", "0x37", "0x6d", "0x8d", "0xd5", "0x4e", "0xa9", "0x6c", "0x56", "0xf4", "0xea", "0x65", "0x7a", "0xae", "0x08"],
    ["0xba", "0x78", "0x25", "0x2e", "0x1c", "0xa6", "0xb4", "0xc6", "0xe8", "0xdd", "0x74", "0x1f", "0x4b", "0xbd", "0x8b", "0x8a"],
    ["0x70", "0x3e", "0xb5", "0x66", "0x48", "0x03", "0xf6", "0x0e", "0x61", "0x35", "0x57", "0xb9", "0x86", "0xc1", "0x1d", "0x9e"],
    ["0xe1", "0xf8", "0x98", "0x11", "0x69", "0xd9", "0x8e", "0x94", "0x9b", "0x1e", "0x87", "0xe9", "0xce", "0x55", "0x28", "0xdf"],
    ["0x8c", "0xa1", "0x89", "0x0d", "0xbf", "0xe6", "0x42", "0x68", "0x41", "0x99", "0x2d", "0x0f", "0xb0", "0x54", "0xbb", "0x16"]
)

inverse_sub_box = (#Standard Rijndael inverse Sbox
    ["0x52", "0x09", "0x6a", "0xd5", "0x30", "0x36", "0xa5", "0x38", "0xbf", "0x40", "0xa3", "0x9e", "0x81", "0xf3", "0xd7", "0xfb"],
    ["0x7c", "0xe3", "0x39", "0x82", "0x9b", "0x2f", "0xff", "0x87", "0x34", "0x8e", "0x43", "0x44", "0xc4", "0xde", "0xe9", "0xcb"],
    ["0x54", "0x7b", "0x94", "0x32", "0xa6", "0xc2", "0x23", "0x3d", "0xee", "0x4c", "0x95", "0x0b", "0x42", "0xfa", "0xc3", "0x4e"],
    ["0x08", "0x2e", "0xa1", "0x66", "0x28", "0xd9", "0x24", "0xb2", "0x76", "0x5b", "0xa2", "0x49", "0x6d", "0x8b", "0xd1", "0x25"],
    ["0x72", "0xf8", "0xf6", "0x64", "0x86", "0x68", "0x98", "0x16", "0xd4", "0xa4", "0x5c", "0xcc", "0x5d", "0x65", "0xb6", "0x92"],
    ["0x6c", "0x70", "0x48", "0x50", "0xfd", "0xed", "0xb9", "0xda", "0x5e", "0x15", "0x46", "0x57", "0xa7", "0x8d", "0x9d", "0x84"],
    ["0x90", "0xd8", "0xab", "0x00", "0x8c", "0xbc", "0xd3", "0x0a", "0xf7", "0xe4", "0x58", "0x05", "0xb8", "0xb3", "0x45", "0x06"],
    ["0xd0", "0x2c", "0x1e", "0x8f", "0xca", "0x3f", "0x0f", "0x02", "0xc1", "0xaf", "0xbd", "0x03", "0x01", "0x13", "0x8a", "0x6b"],
    ["0x3a", "0x91", "0x11", "0x41", "0x4f", "0x67", "0xdc", "0xea", "0x97", "0xf2", "0xcF", "0xcE", "0xf0", "0xb4", "0xe6", "0x73"],
    ["0x96", "0xac", "0x74", "0x22", "0xe7", "0xad", "0x35", "0x85", "0xe2", "0xf9", "0x37", "0xe8", "0x1c", "0x75", "0xdf", "0x6e"],
    ["0x47", "0xf1", "0x1a", "0x71", "0x1d", "0x29", "0xc5", "0x89", "0x6f", "0xb7", "0x62", "0x0e", "0xaa", "0x18", "0xbe", "0x1b"],
    ["0xfc", "0x56", "0x3e", "0x4b", "0xc6", "0xd2", "0x79", "0x20", "0x9a", "0xdb", "0xc0", "0xfe", "0x78", "0xcd", "0x5a", "0xf4"],
    ["0x1f", "0xdd", "0xa8", "0x33", "0x88", "0x07", "0xc7", "0x31", "0xb1", "0x12", "0x10", "0x59", "0x27", "0x80", "0xec", "0x5f"],
    ["0x60", "0x51", "0x7f", "0xa9", "0x19", "0xb5", "0x4a", "0x0d", "0x2d", "0xe5", "0x7a", "0x9f", "0x93", "0xc9", "0x9c", "0xef"],
    ["0xa0", "0xe0", "0x3b", "0x4d", "0xae", "0x2a", "0xf5", "0xb0", "0xc8", "0xeb", "0xbb", "0x3c", "0x83", "0x53", "0x99", "0x61"],
    ["0x17", "0x2b", "0x04", "0x7e", "0xba", "0x77", "0xd6", "0x26", "0xe1", "0x69", "0x14", "0x63", "0x55", "0x21", "0x0c", "0x7d"]
)

def xtime(number):
    """This is the implementation of the multiplication of the byte 02 and its respective polynomial, as each value
    within the Galois field can be represented as a sum of powers of this, this function can be used to carry
    out multiplication within the Galois field and is implemented using a logical bitwise shift and a conditional
    bitwise XOR."""
    if number & 0x80:
        return ((number << 1) ^ 0x1B) & 0xFF
    else:
        return number << 1


class AES:
    """Contains all the code for the AES cipher"""
    def __init__(self):
        """Class constructor"""
        self.original_state = None
        self.current_state = None
        self.original_key = None
        self.round_key = None
        self.round_constant_value = None

    def deal_with_encrypt(self, plaintext, key):
        """Takes plaintext and key from user input, carries out validation and turns the plaintext into a matrix.
        It then defines all of the variables used later within the encryption cycle."""
        if len(plaintext) < 16:
            count = 0
            while len(plaintext) < 16:
                if count == len(key):
                    count = 0
                plaintext += key[count]
                count +=1
        elif len(plaintext) > 16:
            return "Please make sure your plaintext is less than or equal to 16 characters."

        if len(key) < 16:
            return "Key length must be 16"
        print(plaintext)
        self.original_state = convert_message(plaintext)
        self.current_state = convert_message(plaintext)
        self.original_key = convert_message(key)
        self.round_key = self.original_key
        self.round_constant_value = 0
        temp = self.encrypt(self)
        return str(self.hex_to_number(self, temp))

    def hex_to_number(self, list):
        """Converts a matrix of hexadecimal values into decimal values"""
        temp = []
        for i in range(len(list)):
            for j in list[i]:
                temp.append(int(j, 16))
            list[i] = temp
            temp = []
        return list

    def number_to_hex(self, list):
        """Converts a matrix of decimal values into hexidecimal values"""
        temp = []
        for i in range(len(list)):
            for j in list[i]:
                temp.append(hex(j))
            list[i] = temp
            temp = []
        return list

    def encrypt(self):
        """Carries out the encryption. The first pass is just xoring the original state with the key, each remaining
        pass is the same, which is the large loop. The final pass is different, which is why it is carried out outside
        the loop"""
        self.hex_to_number(self, self.original_state)
        self.hex_to_number(self, self.original_key)
        for i in range(4):
            self.current_state[i] = self.xor_columns(self, self.original_key[i], self.original_state[i])
        for i in range(9):
            self.current_state = self.number_to_hex(self, self.current_state)
            for j in range(4):
                self.current_state[j] = self.sub_bytes(self, self.current_state[j])#First SubBytes is applied to the current state.
            self.current_state = self.hex_to_number(self, self.current_state)
            self.shift_rows(self)#ShiftRows is applied to the current state
            self.mix_columns(self)#MixColumns is applied to the current state
            self.generate_round_key(self)#The RoundKey for the current pass is generated
            self.round_constant_value += 1#The RoundConstant is incremented as this changes each round.
            self.apply_round_key(self)#Applies the round key genertated to the current state
        self.current_state = self.number_to_hex(self, self.current_state)
        for j in range(4):
            self.current_state[j] = self.sub_bytes(self, self.current_state[j])#Applies the final SubBytes
        self.current_state = self.hex_to_number(self, self.current_state)
        self.shift_rows(self)#Applies ShiftRows
        self.generate_round_key(self)#Generates the final round key, note MixColumns is skipped in the final round
        self.round_constant_value =0#Resets the round constant to the original
        self.apply_round_key(self)#Applies last round key
        return self.number_to_hex(self, self.current_state)#Returns the encrypted matrix

    def deal_with_decrypt(self, ciphertext, key):
        """Takes in the ciphertext and key, splits the key into a matrix and carries out validation. It then defines
        the variables needed later on for decryption and passes the ciphertext to the decrypt function."""
        temp = [[], [], [], []]
        temp_string = ""
        count = 0
        if len(key) < 16:
            return "Key length must be 16"
        temp_count = 0
        ciphertext += " "
        try:
            for i in ciphertext:
                if i == " ":
                    if len(temp[temp_count]) == 4:
                        temp_count +=1
                    temp[temp_count].append(temp_string)
                    temp_string = ""
                elif i != " ":
                    temp_string += i
        except: return "Please enter a list of 16 numbers to be decrypted"
        try:
            ciphertext = temp
            for i in range(4):
                for j in range(4):
                    ciphertext[i][j] = int(ciphertext[i][j])
        except:
            return "Please enter a list of 16 numbers to be decrypted"
        self.original_state = ciphertext
        self.current_state = ciphertext
        self.original_key = self.hex_to_number(self, convert_message(key))
        self.round_key = [[], [], [], []]
        count2 = 0
        for i in self.original_key:
            for j in i:
                self.round_key[count2].append(j)
            count2 += 1
        self.round_constant_value = 0
        return self.decrypt(self)

    def decrypt(self):
        """Deals with decryption. Generates all of the round keys first and putting them in a list. Then runs all of the
        decryption passes before running the final pass and outputting the plaintext"""
        original_key = [i for i in self.original_key]
        list_of_round_keys = []
        round_key_to_use = 9

        for i in range(10):#Generating all of the round keys at once and putting them in a list
            count = 0
            self.generate_round_key(self)
            self.round_constant_value +=1
            temp3 = [[],[],[],[]]
            for j in self.round_key:
                for k in j:
                    temp3[count].append(k)
                count +=1
            list_of_round_keys.append(temp3)
        self.round_key = list_of_round_keys[round_key_to_use]
        self.apply_round_key(self)#Applies the last round key to the ciphertext, which is the first step to undoing encryption.
        round_key_to_use -=1#Decrements which round key to use as the last key is used first.
        for i in range(9):
            self.inverse_shift_rows(self)#Inverses the shift rows step
            self.current_state = self.number_to_hex(self, self.current_state)
            for i in range(4):#Inverses the subbytes step
                self.current_state[i] = self.inv_sub_bytes(self, self.current_state[i])
            self.current_state = self.hex_to_number(self, self.current_state)
            self.round_key = list_of_round_keys[round_key_to_use]
            self.apply_round_key(self)#Applies the round key which is effectively undoing the round key as applying
            #the roundkey is just XORing the two
            round_key_to_use -= 1#Decrements which round key to use
            self.inv_mix_columns(self, self.current_state)#Inverses the MixColumns step
        self.inverse_shift_rows(self)#Inverses the last shiftrows step
        self.current_state = self.number_to_hex(self, self.current_state)
        for i in range(4):
            self.current_state[i] = self.inv_sub_bytes(self, self.current_state[i])#Inverses the last subbytes step
        self.current_state = self.hex_to_number(self, self.current_state)
        self.round_key = original_key
        self.apply_round_key(self)#Applies the original key to find the plaintext
        return convert_matrix(self.current_state)#Returns the plaintext to the UI.

    def generate_round_key(self):
        """Used to generate the round key. Takes in the last key that was used and generates the next key from it"""
        last_key = [[], [], [], []]
        count = 0
        for i in self.round_key:#Making a copy of the last key used
            for j in i:
                last_key[count].append(j)
            count += 1
        temp = self.round_key[3].pop(0)
        self.round_key[3].append(temp)#Moves the top item of the last column of the matrix to the bottom
        self.round_key = self.number_to_hex(self, self.round_key)
        self.round_key[0] = self.sub_bytes(self, self.round_key[3])#Making the first column of the round key equal to the SubBytes of the 4th column
        self.round_key = self.hex_to_number(self, self.round_key)
        for i, j in zip(range(4), round_constant[self.round_constant_value]):
            self.round_key[0][i] ^= j#Xors the round constant with each value in the first column of the round key
        for i, j, k in zip(self.round_key[0], last_key[0], range(4)):#Finishes the first column of the new round key
            self.round_key[0][k] = i ^ j
        for i in range(1, 4):#Generates the remaining 3 columns based on the first column
            for j in range(4):
                self.round_key[i][j] = self.round_key[i - 1][j] ^ last_key[i][j]

    def xor_columns(self, column1, column2):
        """Performs a logical bitwise XOR on each respective value of two columns"""
        completed_column = []
        for i, j in zip(column1, column2):
            completed_column.append(i^j)
        return completed_column

    def apply_round_key(self):
        """Applies the round key by performing an XOR on each column of the round key and current state."""
        for i,j in zip(range(4), self.round_key):
            self.current_state[i] = self.xor_columns(self, self.current_state[i], j)

    def inv_sub_bytes(self, list):
        """Inverses the SubBytes operation using the Inverse SBox"""
        for i in range(4):
            if len(list[i]) == 3:
                list[i] = list[i][:2] + "0" + list[i][2:]
            row = hex_Values.index(list[i][2])
            column = hex_Values.index(list[i][3])
            byte_to_sub = inverse_sub_box[row][column]
            list[i] = byte_to_sub
        return list

    def sub_bytes(self, list):
        """Carries out the SubBytes operation using the SBox"""
        for i in range(4):
            if len(list[i]) == 3:
                list[i] = list[i][:2] + "0" + list[i][2:]
            row = hex_Values.index(list[i][2])
            column = hex_Values.index(list[i][3])
            byte_to_sub = sub_box[row][column]
            list[i] = byte_to_sub
        return list

    def shift_rows(self):
        """Carries out the ShiftRows step, as each row is shifted a different amount, it shifts each row individually"""
        self.current_state[0][1], self.current_state[1][1], self.current_state[2][1], self.current_state[3][1] = self.current_state[1][1], self.current_state[2][1], self.current_state[3][1], self.current_state[0][1]
        self.current_state[0][2], self.current_state[1][2], self.current_state[2][2], self.current_state[3][2] = self.current_state[2][2], self.current_state[3][2], self.current_state[0][2], self.current_state[1][2]
        self.current_state[0][3], self.current_state[1][3], self.current_state[2][3], self.current_state[3][3] = self.current_state[3][3], self.current_state[0][3], self.current_state[1][3], self.current_state[2][3]

    def inv_mix_columns(self, matrix):
        """The most efficient way of carrying out the Inverse of MixColumns as specified in pg56 in the Design of Rijndael.
        Matrix multiplication is carried out within the Galois field, 2 different values are used alternatively
        for each value in each column, these are determined by xoring these values and then applying xtime twice. After this step is carried
        out, MixColumns occurs. This is the most efficient way of undoing the MixColumns step"""
        temp = matrix
        for i in range(4):
            even = xtime(xtime(temp[i][0]^temp[i][2]))
            odd = xtime(xtime(temp[i][1]^temp[i][3]))
            temp[i][0] ^= even
            temp[i][1] ^= odd
            temp[i][2] ^= even
            temp[i][3] ^= odd
        self.current_state = temp
        return self.mix_columns(self)

    def mix_column(self, matrix):
        """The polynomial is defined by xoring all elements of the column together, and then each value is definded by xoring itself
        with the polynomial which is in turn xord with the xtime result of the current value and the next value. This is used
        to carry out multiplication within the Galois field."""
        temp = matrix
        polynomial = temp[0]^temp[1]^temp[2]^temp[3]
        first_element = temp[0]
        temp[0] ^= polynomial ^ xtime(temp[0] ^ temp[1])
        temp[1] ^= polynomial ^ xtime(temp[1] ^ temp[2])
        temp[2] ^= polynomial ^ xtime(temp[2] ^ temp[3])
        temp[3] ^= polynomial ^ xtime(temp[3] ^ first_element)
        return temp

    def mix_columns(self):
        """Runs MixColumn for each column in the current state."""
        for i in range(4):
            self.current_state[i] = self.mix_column(self, self.current_state[i])



    def inverse_shift_rows(self):
        """Inverses the shift rows step by shifting each row in the opposite direction by the same amount as before"""
        self.current_state[0][1], self.current_state[1][1], self.current_state[2][1], self.current_state[3][1] = self.current_state[3][1], self.current_state[0][1], self.current_state[1][1], self.current_state[2][1]
        self.current_state[0][2], self.current_state[1][2], self.current_state[2][2], self.current_state[3][2] = self.current_state[2][2], self.current_state[3][2], self.current_state[0][2], self.current_state[1][2]
        self.current_state[0][3], self.current_state[1][3], self.current_state[2][3], self.current_state[3][3] = self.current_state[1][3], self.current_state[2][3], self.current_state[3][3], self.current_state[0][3]












